from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),

    path('', views.index, name='index'),
    path('nba/', views.nba, name='nba'),
    path('nba/tweets', views.nba_tweets, name='nba_tweets'),
    path('mlb/tweets/add-mlb-user', views.add_twitter_user, name='add_twitter_user'),
    path('nba/tweets/add-nba-user', views.add_twitter_user, name='add_twitter_user'),
    path('mlb/', views.mlb, name='mlb'),
    path('mlb/tweets', views.mlb_tweets, name='mlb_tweets'),
    path('mlb/<str:team_name>/', views.mlb_team, name='mlb_team'),

    # path('mlb/tweets/<str:user>', views.add_twitter_user, name='add_twitter_user'),
    #path('get_teams/', views.get_teams, name='get_teams'),
]