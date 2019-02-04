from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='cluster'),
   # url(r'^$', views.loadNet, name='inicio_red'),
]
