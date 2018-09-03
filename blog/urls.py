from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^resume$', views.resume, name='resume'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^portfolio/calculator$', views.calculator, name='calculator'),
    url(r'^portfolio/game$', views.game, name='game'),
    url(r'^portfolio/image_viewer$', views.image_viewer, name='image'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^design$', views.design, name='design'),
    url(r'^board$', views.PostListView.as_view(), name='board'),
    url('^post/(?P<pk>[0-9]+)/$', views.postDetailView.as_view(), name='post_detail'),
    url(r'^post/new$', views.post_new, name='post_new'),

]
