from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from account.forms import Sign_Up
from activities import views
from .models import User_Account

# Create your views here.
def my_sign_in(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

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
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_account = User_Account.objects.create(
                user_id = request.user,
                student_id = form.cleaned_data.get('student_id'),
            )
            return redirect('/index/')
    else:
        form = Sign_Up()
    return render(request, 'sign_up.html', {'form': form})

def my_logout(request):
    logout(request)
    return redirect('/index/')

