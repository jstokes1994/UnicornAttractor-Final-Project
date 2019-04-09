from django.shortcuts import render, redirect
from .models import Feature
from .forms import AddFeature
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
    
@login_required    
def add_feature(request):
    if request.method == 'POST':
        form = AddFeature(request.POST)
        if form.is_valid():
            new_feature = form.save(commit=False)
            new_feature.author = request.user
            new_feature.money_donated = 10
            new_feature.save()
            return(redirect('features'))
    else:
        form = AddFeature()
    return render(request, "add_feature.html", {'form': form})
    
@login_required
def features(request):
    # Returns all of the features in the database
    features = Feature.objects.all().order_by('-created_date')
    return render(request, "features.html", {'features': features})
    
@login_required
def single_feature(request, feature_id):
    # Returns the information about a single feature
    feature = Feature.objects.get(id=feature_id)
    user_id = request.user.id
    if request.GET.get('Upvote') == 'Upvote':
        if feature.votes.exists(user_id):
            messages.error(request,'You have already voted!')
        else:
            feature.votes.up(user_id)
            feature.money_donated += 10
            feature.save()
            
            messages.error(request,'Thanks for your donation!')
        
    return render(request, "feature_page.html", {'feature': feature})