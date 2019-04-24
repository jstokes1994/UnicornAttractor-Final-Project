from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/', default='images/default-avatar.png', null=True)
    
    def __str__(self):
        return self.user.username

