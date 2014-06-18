from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse
from home.models import *
from allauth.socialaccount.models import SocialAccount

def index(request):
	wagers = WagerParticipant.objects.filter(user_id=request.user.id)
	return render(request, 'home/index.html', {'wagers': wagers})

def getUserWagers(request):
	queryset = WagerParticipant.objects.filter(user_id=request.user.id)
	return HttpResponse(queryset)

def getContests(request):
	contests = Contest.objects.all()
	queryset = {
		'contests' : contests
	}
	return render(request, 'home/contests.html', {'queryset': queryset})
	
def getWager(request, wager_id):
	wager = Wager.objects.get(pk=wager_id)
	wager_participants = WagerParticipant.objects.filter(wager_id=wager_id)
	queryset = {
		'wager' : wager,
		'wager_participants' : wager_participants,
		'request' : request
	}
	return render(request, 'home/wager.html', {'queryset': queryset})

def getFriends(request):
  
  cookie = facebook.get_user_from_cookie(request.cookies, '1404290166525727', 'b9f7aa28edface3992246d9de82ea2cd')
  graph = facebook.GraphAPI(cookie["access_token"])
  
  sa = SocialAccount.objects.filter(user_id=request.user.id)[0]
  
  g = facebook.GraphAPI('1404290166525727|ZOiRt0-wS_S-qd4er1v608SlxHE')
  friends = g.get_connections(sa.uid, 'friends')
  
  queryset = {
    'user_id': request.user.id,
    'user': sa.uid,
    'friends': [f[0]['name'] for f in friends['data']],
  }
  return render(request, 'home/friends.html', {'queryset': queryset})