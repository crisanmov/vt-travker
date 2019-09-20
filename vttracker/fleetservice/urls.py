from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/$', views.fleetAdmin, name='fleetAdmin'),
    url(r'^flotilla/$', views.driverIndex, name='driverIndex'),
    url(r'^get_users/$', views.getUsers, name='getUsers'),
    url(r'^create_driver/$', views.createDriver, name='createDriver'),
]
