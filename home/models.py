from django.db import models
from django.contrib.auth.models import User
from agw import settings

# Create your models here.

class Contest(models.Model):
	description = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	contest_close_date = models.DateTimeField(null=True, blank=True) 
	contest_open_date = models.DateTimeField(null=True, blank=True) 
	created_at = models.DateTimeField(auto_now=True) 
	modified_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.description

class ContestSide(models.Model):
	contest = models.ForeignKey(Contest)
	participant = models.TextField(null=True, blank=True)
	outcome = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now=True) 
	modified_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.participant 
			
class Wager(models.Model):
	wagered_by = models.ForeignKey(settings.AUTH_USER_MODEL)
	description = models.TextField(null=True, blank=True)
	amount = models.FloatField(null=True, blank=True)
	is_settled = models.BooleanField(default=False)
	contest = models.ForeignKey(Contest)
	created_at = models.DateTimeField(auto_now=True) 
	modified_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.description 

class WagerParticipant(models.Model):
	wager = models.ForeignKey(Wager)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	description = models.TextField(null=True, blank=True)
	contest_side = models.ForeignKey(ContestSide)
	accepted = models.BooleanField(default=False)
	invitation_uid = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now=True) 
	modified_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.wager)