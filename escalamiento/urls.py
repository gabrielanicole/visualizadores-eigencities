from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio_escalamiento, name='inicio_escalamiento'),
    url(r'^variable$', views.index, name='escalamiento'),    
    url(r'^ciudad/(?P<pk>\d+)$', views.ciudad, name='ciudad'),
]