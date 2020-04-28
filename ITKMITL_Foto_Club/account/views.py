

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from account.forms import EquipmentForm, Sign_Up, suggestionForm
from activities import views

from .models import Equipment, User_Account, suggestion


# Create your views here.
def role_check_super(user):
    return user.is_superuser
    
def role_check_member(user):
    return user.is_staff

def my_sign_in(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/index/')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, template_name='sign_in.html', context=context)

def my_sign_up(request):
    if request.method == 'POST':
        form = Sign_Up(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, is_active=True)
            login(request, user)
            user_account = User_Account.objects.create(
                user_id = request.user,
                student_id = request.POST.get('student_id'),
                picture_path = request.FILES['picture'],
                pass_code = request.POST.get('pass_code'),
            )
            return redirect('/index/')
    else:
        form = Sign_Up()
    return render(request, 'sign_up.html', {'form': form})

def my_logout(request):
    logout(request)
    return redirect('/index/')

def my_passwordRecovery(request):
    if request.method == "POST":
        username = request.POST.get('username')
        sid = request.POST.get('std')
        newpw = request.POST.get('pw')
        passcode = request.POST.get('passcode')
        u = User.objects.get(username = username)
        un = User_Account.objects.get(student_id = sid)
        if u.id == un.user_id_id and un.pass_code == passcode:
            u.set_password(newpw)
            u.save()
            return redirect('/sign_in/')
    return render(request, 'passwordRecovery.html')

@login_required(login_url='/sign_in/')
def views_audience(request):
    p_request = User_Account.objects.all()
    return render(request, 'view_audience.html', context={'p_request':p_request})

@user_passes_test(role_check_super)
def add_member(requset,id):
    add_to = User_Account.objects.get(pk=id)
    add_to.member = True
    add_to.save()
    user = User.objects.get(pk=add_to.user_id.id)
    user.is_staff = True
    user.save()

    if add_to.member == True:
        return redirect('/view_audience/')

@login_required(login_url='/sign_in/')
def create_suggestion(request):
    suggest = suggestionForm(request.POST)
    if request.method == "POST":
        if suggest.is_valid():
            a = suggestion.objects.create(
            title = request.POST.get('title'),
            detail = request.POST.get('detail')
        )
        return redirect('/index/')
    context = {'form': suggest}
    return render(request, 'suggestion.html', context)  

@user_passes_test(role_check_super)
def view_suggestion(request):
    suggest = suggestion.objects.all()
    context = {'suggest' : suggest}
    return render(request, 'view_suggestion.html', context)

@user_passes_test(role_check_member)
def add_Equipment(request):
    current_user = request.user
    equipment_formset = formset_factory(EquipmentForm, extra = 2)
    if request.method == "POST":
        formset = equipment_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('del_flag'):
                    equip = Equipment.objects.get(pk = form.cleaned_data['equip_id'])
                    equip.delete()
                    continue
                if form.cleaned_data.get('equip_id'):
                    equip = Equipment.objects.get(pk = form.cleaned_data['equip_id'])
                    equip.equipment_type = form.cleaned_data['equipment_type']
                    equip.equipment_detail = form.cleaned_data['equipment_detail']
                    equip.equipment_title = form.cleaned_data['equipment_title']
                    equip.save()

                else:
                     if form.cleaned_data.get('equipment_title'):    
                        equip = Equipment.objects.create(
                            equipment_type = form.cleaned_data['equipment_type'],
                            equipment_detail = form.cleaned_data['equipment_detail'],
                            equipment_title = form.cleaned_data['equipment_title'],
                            user_id = current_user
                        )
        return redirect('/view_equipment/')
    else:
        a = Equipment.objects.filter(user_id = current_user.id)
        data = []
        for i in a:
            a_dict = {
                'equip_id' : i.id,
                'equipment_type' : i.equipment_type,
                'equipment_detail' : i.equipment_detail,
                'equipment_title' : i.equipment_title
            }
            data.append(a_dict)
        formset = equipment_formset(initial = data)
        
    return render(request, 'equipment.html', context={'formset':formset})

@user_passes_test(role_check_member)
def view_Equipment(request):
    eqip = Equipment.objects.all().order_by('user_id')
    return render(request, 'view_equipment.html', context={'eqip':eqip})
