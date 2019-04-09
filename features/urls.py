from django.conf.urls import url, include
from .views import add_feature, features, single_feature

urlpatterns = [
    url(r'^$', features, name='features'),
    url(r'^add_feature/$', add_feature, name='add_feature'),
    url(r'^single_feature/(?P<feature_id>\d+)/$', single_feature, name='single_feature'),
    ]
