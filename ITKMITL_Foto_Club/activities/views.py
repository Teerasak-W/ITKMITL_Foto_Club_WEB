from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from account.models import Request
from .models import Activities
from .forms import Create_Activities, Request_Activities

# Create your views here.

def index(request):
    user_view = request.user
    activities = Activities.objects.all()
    # print(activities)
    return render(request, 'index.html', context={'user_view': user_view,'activities': activities})

def createSuggestion(request):
    #if request.method == "POST":
    return render(request, 'suggestion.html')

def view_activities(request,activities_id):
    activities = Activities.objects.get(pk = activities_id)
    return render(request, 'activities.html', context={
        'activities' : activities,
        'activities_id': activities_id,
    })
def create_activities(request):
    if request.method == 'POST':
        form = Create_Activities(request.POST)
        if form.is_valid():
        # try:
        #     upload_file = request.FILES['picfile']
        #     fs = FileSystemStorage()
        #     name = fs.save(upload_file.name, upload_file)
        #     url = fs.url(name)
        # except MultiValueDictKeyError:
        #     upload_file = False
        #     url = '\media\default.PNG'
        # print(url)
            activities = Activities.objects.create(
                activity_title = request.POST.get('activity_title'),
                # picture_path = request.POST.get('picture_path'),
                location = request.POST.get('location'),
            )
            print(activities)
            if activities:
                return redirect('/index/')
    else:
        form = Create_Activities()
        print(form)
    return render(request, 'create_activities.html', {'form': form})

def request_activities(request):
    if request.method == 'POST':
        form = Request_Activities(request.POST)
        if form.is_valid():
            request_activities = Request.objects.create(
                request_title = request.POST.get('request_title'),
                location = request.POST.get('location'),
                picture_path = request.POST.get('picture_path'),
                detail = request.POST.get('detail'),
            )
            print(request_activities)
            if request_activities:
                return redirect('/index/')
    else:
        form = Request_Activities()
        print(form)
    return render(request, 'request_activities.html', {'form': form})

def view_request(request):
    v_request = Request.objects.all()
    # print(activities)
    return render(request, 'view_request.html', context={'v_request': v_request})


