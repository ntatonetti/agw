from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^wager/(?P<wager_id>[0-9]+)$', views.getWager, name='getWager'),
	url(r'^contests/$', views.getContests, name='getContests'),
  url(r'^friends/$', views.getFriends, name='getFriends')
)