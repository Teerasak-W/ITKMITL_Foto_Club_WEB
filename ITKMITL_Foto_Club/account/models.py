from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_Account(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    student_id = models.CharField(max_length=8)
    picture_path = models.FileField(upload_to='user')
    pass_code = models.CharField(max_length=5)
    audience = models.BooleanField(default=True)
    member = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

class Equipment(models.Model):
    type_for = (('0', 'camera'),('1', 'lens'),('2', 'light'),('3', 'other'))
    equipment_type = models.CharField(max_length=1, choices=type_for)
    equipment_detail = models.TextField()
    equipment_title = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Request(models.Model):
    request_title = models.CharField(max_length=50)
    location = models.TextField()
    picture_path = models.FileField(upload_to='activities')
    detail = models.TextField()
    request_status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Request_contact(models.Model):
    ar_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)

class Request_datetime(models.Model):
    ar_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

class suggestion(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
