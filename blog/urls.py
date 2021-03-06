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
    url(r'^save_board$', views.savePostListView.as_view(), name='save_board'),
    url('^post/(?P<pk>[0-9]+)/$', views.postDetailView.as_view(), name='post_detail'),
    url(r'^post/new$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]
