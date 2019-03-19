from django import forms
from .models import Feature

class AddFeature(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'description']
        labels = {
            'name': ('What do you want the feature to be called?'),
            'description': ('Describe your feature')
        }
