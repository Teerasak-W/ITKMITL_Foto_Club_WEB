from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Activities(models.Model):
    activity_title = models.CharField(max_length=50)
    picture_path = models.URLField(max_length = 500,null = True) 
    location = models.TextField()

class Staff(models.Model):
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    
class Album(models.Model):
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    album_name = activity_title = models.CharField(max_length=50)

class Picture(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    album_name = activity_title = models.CharField(max_length=50)
    picture_path = models.URLField(max_length = 500,null = True)

class Contact(models.Model):
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)

class Datetime(models.Model):
    start_time = DateTimeField(auto_now=True)
    finish_time = DateTimeField(auto_now=True)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)

    
