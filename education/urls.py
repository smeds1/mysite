from django.urls import path
from . import views

app_name = 'education'
urlpatterns = [
	path('', views.index, name='index'),
	path('states/', views.states, name='states'),
	path('demographics/', views.demographics, name='demographics'),
	path('demographics/<group>/', views.demographic_detail, name='demographic_detail'),
	path('states/<state_abbr>/', views.state_detail, name='state_detail'),
    path('stats/', views.stats, name='stats'),
]
