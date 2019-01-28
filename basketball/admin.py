from django.contrib import admin

from .models import Bracket, Team, Tournament, Season_stats, Participant
from .forms import MyBracketAdminForm

class BracketAdmin(admin.ModelAdmin):
	"""
	Custom form for Bracket model on admin page
	"""
	form = MyBracketAdminForm

class TournamentAdmin(admin.ModelAdmin):
	"""
	Form organization for Tournament model on admin page
	"""
	fieldsets = [
		(None, {'fields': ['year']}),
		('Region Configuration', {'fields': ['top_left_region','bottom_left_region','top_right_region','bottom_right_region']}),
		('Top Left', {'fields': ['top_left_1', 'top_left_16','top_left_8','top_left_9','top_left_5','top_left_12','top_left_4','top_left_13',
					'top_left_6', 'top_left_11','top_left_3','top_left_14','top_left_7','top_left_10','top_left_2','top_left_15']}),
		('Bottom Left',{'fields': ['bottom_left_1', 'bottom_left_16','bottom_left_8','bottom_left_9','bottom_left_5','bottom_left_12','bottom_left_4','bottom_left_13',
					'bottom_left_6', 'bottom_left_11','bottom_left_3','bottom_left_14','bottom_left_7','bottom_left_10','bottom_left_2','bottom_left_15']}),
		('Top Right', {'fields': ['top_right_1', 'top_right_16','top_right_8','top_right_9','top_right_5','top_right_12','top_right_4','top_right_13',
					'top_right_6', 'top_right_11','top_right_3','top_right_14','top_right_7','top_right_10','top_right_2','top_right_15']}),
		('Bottom Right', {'fields': ['bottom_right_1', 'bottom_right_16','bottom_right_8','bottom_right_9','bottom_right_5','bottom_right_12','bottom_right_4','bottom_right_13',
					'bottom_right_6', 'bottom_right_11','bottom_right_3','bottom_right_14','bottom_right_7','bottom_right_10','bottom_right_2','bottom_right_15']}),
	]

#register models to be added/updated/deleted via admin page
admin.site.register(Team)
admin.site.register(Bracket, BracketAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Season_stats)
admin.site.register(Participant)
