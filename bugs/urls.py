from django.conf.urls import url, include
from .views import add_bug, bugs, single_bug

urlpatterns = [
    url(r'^$', bugs, name='bugs'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
    url(r'^single_bug/(?P<bug_id>\d+)/$', single_bug, name='single_bug')
    ]
