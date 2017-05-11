from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url(r'^Create/', views.create, name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='create'),
    url(r'^$', views.index, name='index'),
    url(r'^impressum/$', views.impressum, name='index'),

]