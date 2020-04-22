"""ITKMITL_Foto_Club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from activities import views as actv
from account import views as accv

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', actv.index),
    path('index/', actv.index),
    path('activities/', actv.view_activities, name='activities'),
    path('create_activities/', actv.create_activities, name='create_activities'),
    path('request_activities/', actv.request_activities, name='request_activities'),
    path('request_add/<int:id>', actv.request_add, name='request_add'),
    path('view_request/', actv.view_request, name='view_request'),

    path('sign_in/', accv.my_sign_in, name='sign_in'),
    path('logout/', accv.my_logout, name='logout'),
    path('sign_up/', accv.my_sign_up, name='sign_up'),
    path('suggestion/', actv.createSuggestion, name='suggestion'),
]