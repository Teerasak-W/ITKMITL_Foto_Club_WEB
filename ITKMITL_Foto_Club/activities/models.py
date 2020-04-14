from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Activities(models.Model):
    activity_title = models.CharField(max_length=50)
    picture_path = models.URLField(max_length = 500,null = True) 
    location = models.TextField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Staff(models.Model):
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)