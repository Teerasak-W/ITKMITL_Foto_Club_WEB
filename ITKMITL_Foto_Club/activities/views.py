from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def index(request):
    user_view = request.user
    return render(request, 'index.html', context={'user_view': user_view,})