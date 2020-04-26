from django.db import models
from django.contrib.auth.models import User
from account.models import Request
# Create your models here.
class Activities(models.Model):
    activity_title = models.CharField(max_length=50)
    picture_path = models.FileField(upload_to='activities')
    location = models.TextField()
    rq_id = models.ForeignKey(Request, on_delete=models.CASCADE)


class Staff(models.Model):
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    
class Album(models.Model):
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=50)

class Picture(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    picture_path = models.FileField(upload_to='album')

class Contact(models.Model):
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)

class Date_time(models.Model):
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()



    
