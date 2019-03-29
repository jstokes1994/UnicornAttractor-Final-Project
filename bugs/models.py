from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from vote.models import VoteModel

# Create your models here.

class Bug(VoteModel, models.Model):
    status_choices = (
        ('N', 'Not Started'),
        ('I', 'In Development'),
        ('D', 'Done')
    )
    
    name = models.CharField(max_length=26, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_choices, default='N')
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
        
class BugsComments(models.Model):
    """Model migration design for comments"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature = models.ForeignKey(Bug, on_delete=models.CASCADE)
    date_of_comment = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=2000, blank=False)
    
    

