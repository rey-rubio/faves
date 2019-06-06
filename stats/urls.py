from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),

    path('', views.index, name='index'),
    path('nba/', views.nba, name='nba'),
    path('mlb/', views.mlb, name='mlb'),
    # path('mlb/<string:team_name>/', views.mlb_team, name='team'),
    #path('get_teams/', views.get_teams, name='get_teams'),
]