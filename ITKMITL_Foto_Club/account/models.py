from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Request(models.Model):
    request_title = models.CharField(max_length=50)
    location = models.TextField()
    picture_path = models.URLField(max_length = 500,null = True) 
    detail = models.TextField()
    request_status = models.BooleanField(default=False)

class Equipment(models.Model):
    type_for = (('Ca', 'camera'),('Le', 'lens'),('Si', 'light'),('Ot', 'other'))
    equipment_type = models.CharField(max_length=2, choices=type_for)
    equipment_detail = models.TextField()
    equipment_title = models.CharField(max_length=50)

class Date_time(models.Model):
    start_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(auto_now=True)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
