from django.contrib import admin
#from home.models import UserProfile
from home.models import *

class ContestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestSide)
admin.site.register(Wager)
admin.site.register(WagerParticipant)