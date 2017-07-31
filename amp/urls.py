from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^profile/', views.profile, name = 'profile'),
    url(r'^messaging/', views.messaging, name = 'messaging'),

]
