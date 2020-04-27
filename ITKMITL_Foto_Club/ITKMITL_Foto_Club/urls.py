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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from activities import views as actv
from account import views as accv

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', actv.index),
    path('index/', actv.index, name='index'),


    path('activities/<int:id>/', actv.view_activities, name='activities'),
    path('activities/album/<int:at_id>/<int:id>/', actv.view_album, name='view_album'),
    path('create_activities/<int:id>/', actv.create_activities, name='create_activities'),
    path('request_activities/', actv.request_activities, name='request_activities'),
    path('view_request/', actv.view_request, name='view_request'),
    path('view_request/add_time/<int:id>/', actv.add_time, name='add_time'),
    path('view_request/add_contact/<int:id>/', actv.add_contact, name='add_contact'),
    path('view_request/add_staff/<int:id>/', actv.add_staff, name='add_staff'),
    path('add_album/<int:id>/', actv.add_album, name='add_album'),
    path('add_picture/<int:at_id>/<int:id>/', actv.add_picture, name='add_picture'),
    path('remove_picture/<int:at_id>/<int:id>/<int:pic_id>/', actv.remove_picture, name='remove_picture'),


    path('sign_in/', accv.my_sign_in, name='sign_in'),
    path('logout/', accv.my_logout, name='logout'),
    path('sign_up/', accv.my_sign_up, name='sign_up'),
    path('view_audience/', accv.views_audience, name='view_audience'),
    path('add_member/<int:id>/', accv.add_member, name='add_member'),
    path('suggestion/', accv.create_suggestion, name='suggestion'),
    path('view_suggestion/', accv.view_suggestion, name='view_suggestion'),
    path('eqip/' ,accv.add_Equipment, name='equipment'),
    path('view_eqip/' ,accv.view_Equipment, name='view_equipment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    