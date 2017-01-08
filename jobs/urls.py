from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'jobs/', views.jobs, name='jobs'),
    url(r'^candidate/(?P<candidate_name>[^/]+)/$', views.candidate, name='candidate'),
    url(r'^search/$', views.search, name='search'),
    url(r'^download/(?P<location>[^/]+)/(?P<skills>[^/]+)/$', views.some_view, name='download'),
]