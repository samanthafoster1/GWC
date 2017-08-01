from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^playlist/(?P<pk>\d+)/$', views.playlist, name = 'playlist'),

]
