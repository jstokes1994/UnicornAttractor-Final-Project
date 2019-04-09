from django.shortcuts import render
from features.models import Feature
from bugs.models import Bug
from accounts.models import User
from django.db.models import Count

# Create your views here.

def graphs(request):
    
    all_features = Feature.objects.count()
    all_users = User.objects.count()
    all_bugs = Bug.objects.count()
    
    top_paid_features = Feature.objects.order_by('-money_donated').values('name', 'money_donated')[:5]

    most_paid_name_1 = top_paid_features[0]['name']
    most_paid_name_2 = top_paid_features[1]['name']
    most_paid_name_3 = top_paid_features[2]['name']
    most_paid_name_4 = top_paid_features[3]['name']
    most_paid_name_5 = top_paid_features[4]['name']
    
    most_paid_money_1 = top_paid_features[0]['money_donated']
    most_paid_money_2 = top_paid_features[1]['money_donated']
    most_paid_money_3 = top_paid_features[2]['money_donated']
    most_paid_money_4 = top_paid_features[3]['money_donated']
    most_paid_money_5 = top_paid_features[4]['money_donated']
    
    top_liked_bugs = Bug.objects.order_by('-likes').values('name', 'likes')[:5]
    
    most_liked_bug_name_1 = top_liked_bugs[0]['name']
    most_liked_bug_name_2 = top_liked_bugs[1]['name']
    most_liked_bug_name_3 = top_liked_bugs[2]['name']
    most_liked_bug_name_4 = top_liked_bugs[3]['name']
    most_liked_bug_name_5 = top_liked_bugs[4]['name']
    
    most_liked_bug_likes_1 = top_liked_bugs[0]['likes']
    most_liked_bug_likes_2 = top_liked_bugs[1]['likes']
    most_liked_bug_likes_3 = top_liked_bugs[2]['likes']
    most_liked_bug_likes_4 = top_liked_bugs[3]['likes']
    most_liked_bug_likes_5 = top_liked_bugs[4]['likes']
    
    
    status_features = Feature.objects.values('status').annotate(Count('status')).order_by('status')
    done_status_features = status_features[0]['status__count']
    dev_status_features = status_features[1]['status__count']
    nd_status_features = status_features[2]['status__count']
    
    status_bugs = Bug.objects.values('status').annotate(Count('status')).order_by('status')
    done_status_bugs = status_bugs[0]['status__count']
    dev_status_bugs = status_bugs[1]['status__count']
    nd_status_bugs = status_bugs[2]['status__count']
    
    overall_done_status = done_status_features + done_status_bugs
    overall_dev_status = dev_status_features + dev_status_bugs
    overall_nd_status = nd_status_features + nd_status_bugs
    
    
    return render(request, 'graphs.html', 
    {'all_features': all_features, 'all_users': all_users, 'all_bugs': all_bugs,
        'most_paid_name_1': most_paid_name_1,
        'most_paid_name_2': most_paid_name_2,
        'most_paid_name_3': most_paid_name_3,
        'most_paid_name_4': most_paid_name_4,
        'most_paid_name_5': most_paid_name_5,
        'most_paid_money_1': most_paid_money_1,
        'most_paid_money_2': most_paid_money_2,
        'most_paid_money_3': most_paid_money_3,
        'most_paid_money_4': most_paid_money_4,
        'most_paid_money_5': most_paid_money_5,
        'most_liked_bug_name_1': most_liked_bug_name_1,
        'most_liked_bug_name_2': most_liked_bug_name_2,
        'most_liked_bug_name_3': most_liked_bug_name_3,
        'most_liked_bug_name_4': most_liked_bug_name_4,
        'most_liked_bug_name_5': most_liked_bug_name_5,
        'most_liked_bug_likes_1': most_liked_bug_likes_1,
        'most_liked_bug_likes_2': most_liked_bug_likes_2,
        'most_liked_bug_likes_3': most_liked_bug_likes_3,
        'most_liked_bug_likes_4': most_liked_bug_likes_4,
        'most_liked_bug_likes_5': most_liked_bug_likes_5,
        'overall_done_status': overall_done_status,
        'overall_dev_status': overall_dev_status,
        'overall_nd_status': overall_nd_status
        
    })
