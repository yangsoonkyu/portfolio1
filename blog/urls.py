from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^game$', views.game, name='game'),
    url(r'^calculator$', views.calculator, name='calculator'),
    url(r'^image_viewer$', views.image_viewer, name='image_viewer'),
    url(r'^contact$', views.contact, name='contact'),

    ]