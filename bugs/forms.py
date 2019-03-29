from django import forms
from .models import Bug

class AddBug(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name', 'description']
        labels = {
            'name': ('What do you want the bug to be called?'),
            'description': ('Describe your bug')
        }
