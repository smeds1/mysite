from django.urls import path
from . import views

app_name = 'basketball'
urlpatterns = [
    path('', views.index, name='index'),
	path('teams/', views.teams, name='teams'),
	path('tournaments/', views.tournaments, name='tournaments'),
	path('tournament/<int:year>/', views.tournament_detail, name='tournament_detail'),
	path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
	path('bracket/<int:bracket_id>/', views.bracket, name='bracket'),
    path('stats/', views.stats, name='stats'),
    path('participant/<name>',views.participant,name='participant'),
    path('ajax/stats_graph/', views.stats_graph, name='stats_graph'),
]
