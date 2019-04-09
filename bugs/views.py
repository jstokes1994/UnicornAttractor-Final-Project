from django.shortcuts import render, redirect
from .models import Bug
from .forms import AddBug
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required    
def add_bug(request):
    if request.method == 'POST':
        form = AddBug(request.POST)
        if form.is_valid():
            new_bug = form.save(commit=False)
            new_bug.author = request.user
            new_bug.save()
            return(redirect('bugs'))
    else:
        form = AddBug()
    return render(request, "add_bug.html", {'form': form})

@login_required
def bugs(request):
    # Returns all of the bugs in the database
    bugs = Bug.objects.all().order_by('-created_date')
    return render(request, "bugs.html", {'bugs': bugs})
    
@login_required
def single_bug(request, bug_id):
    # Returns the information about a single bug
    bug = Bug.objects.get(id=bug_id)
    user_id = request.user.id
    print(user_id)
    if request.GET.get('Like') == 'Like':
        if bug.votes.exists(user_id):
            messages.error(request,'You have already liked this!')
        else:
            bug.votes.up(user_id)
            bug.likes += 1
            bug.save()
    print(bug.votes.count())
    return render(request, "bug_page.html", {'bug': bug})
    
