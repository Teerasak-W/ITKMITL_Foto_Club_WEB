from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from account.models import Request, User_Account, Request_contact, Request_datetime
from .models import Activities, Date_time, Contact, Staff, Album, Picture
from .forms import Request_Activities, Request_Datetime, Request_Contact

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user_view = User_Account.objects.get(user_id = request.user)
    else:
        user_view = request.user
    activities = Activities.objects.all()
    print(request.user)
    return render(request, 'index.html', context={'user_view': user_view,'activities': activities})

def view_activities(request,id):
    activities = Activities.objects.get(pk = id)
    staff = Staff.objects.filter(activity_id = activities.rq_id)
    album = Album.objects.filter(activity_id = activities.id)
    for a in staff:
        status = (a.staff_id == request.user)
        if status:
            break
        else:
            status = False
    print(status)
    return render(request, 'activities.html', context={
        'activities' : activities,
        'id': id,
        'staff':staff,
        'album':album,
        'status':status,
    })
    
def create_activities(request,id):
    v_request = Request.objects.get(pk = id)
    c_request = Request_contact.objects.filter(ar_id = id)
    t_request = Request_datetime.objects.filter(ar_id = id)
    activities = Activities.objects.create(
        activity_title = v_request.request_title,
        location = v_request.location,
        picture_path = v_request.picture_path,
        rq_id = v_request,
    )
    for c in c_request:
        contact = Contact.objects.create(
            activity_id = activities,
            contact_person = c.name,
            contact_number = c.number,
        )
    for t in t_request:
        date_time = Date_time.objects.create(
            activity_id = activities,
            start_time = t.start_time,
            finish_time = t.start_time,
        )
    v_request.request_status = True
    v_request.save()
    if activities:
        return redirect('/index/')

def request_activities(request):
    if request.method == 'POST':
        form_RA = Request_Activities(request.POST)
        if form_RA.is_valid():
            request_activities = Request.objects.create(
                request_title = request.POST.get('request_title'),
                location = request.POST.get('location'),
                picture_path = request.FILES['picture_path'],
                detail = request.POST.get('detail'),
                user_id = request.user,
            )
            print(request.FILES['picture_path'])
        if request_activities:
            return redirect('/index/')

    else:
        form_RA = Request_Activities()
    return render(request, 'request_activities.html', context={'form_RA': form_RA,})

def add_contact(request,id):
    if request.method == 'POST':
        form_CT = Request_Contact(request.POST)
        if form_CT.is_valid():
            request_contact = Request_contact.objects.create(
                name = request.POST.get('contact_person'),
                number = request.POST.get('contact_number'),
                ar_id = Request.objects.get(pk = id),
            )
        if request_contact:
            return redirect('/view_request/')
    else:
        form_CT = Request_Contact()
    return render(request, 'add_contact.html', {'form_CT':form_CT})

def add_time(request,id):
    if request.method == 'POST':
        form_DT = Request_Datetime(request.POST)
        if form_DT.is_valid():
            request_datetime = Request_datetime.objects.create(
                start_time = request.POST.get('start_time'),
                finish_time = request.POST.get('finish_time'),
                ar_id = Request.objects.get(pk = id),
            )
        if request_datetime:
            return redirect('/view_request/')
    else:
        form_DT = Request_Datetime()
    return render(request, 'add_time.html', {'form_DT':form_DT})

def view_request(request):
    v_request = Request.objects.all()
    u_request = User_Account.objects.get(user_id = request.user.id)
    c_request = Request_contact.objects.all()
    t_request = Request_datetime.objects.all()
    s_request = Staff.objects.all()
    return render(request, 'view_request.html', context={
        'v_request':v_request,
        'u_request':u_request,
        'c_request':c_request,
        't_request':t_request,
        's_request':s_request,
        })

def add_staff(request,id):
    staff = Staff.objects.create(
        staff_id = request.user,
        activity_id = Request.objects.get(pk = id),
    )
    return redirect('/view_request/')
    
def add_album(request,id):
    album = Album.objects.create(
        activity_id = Activities.objects.get(pk = id),
        album_name = request.POST.get('album_name'),
    )
    return redirect('/activities/%d/'%id)

def view_album(request,at_id,id):
    album = Album.objects.filter(id=id)
    staff = Staff.objects.filter(activity_id = at_id)
    pic = Picture.objects.filter(album_id=id)
    for a in staff:
        status = (a.staff_id == request.user)
        if status:
            break
        else:
            status = False
    print(status)
    return render(request, 'view_album.html', context={'album':album,'pic':pic,'staff':staff, 'status':status})

def add_picture(request,at_id,id):
    album_name = request.FILES.getlist('picture_name')
    for i in album_name:
        picture = Picture.objects.create(
            album_id = Album.objects.get(pk = id),
            picture_path = i,
        )
    return redirect('/activities/album/%d/%d'%(at_id,id))

def remove_picture(request,at_id,id,pic_id):
    picture = Picture.objects.get(pk=pic_id)
    picture.delete()
    return redirect('/activities/album/%d/%d'%(at_id,id))

def validate_request_title(request):
    username = request.GET.get('request_title', None)
    data = {
        'is_taken': Request.objects.filter(request_title=username).exists()
    }
    return JsonResponse(data)