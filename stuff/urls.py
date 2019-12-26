from django.urls import path

from .templates.views import *

app_name = 'stuff'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),

    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('influencers', influencers, name='influencers'),
    path('influencers/<str:influencer_id>', influencer, name='influencer'),
    path('nba', nba, name='nba'),
    path('nba/tweets', nba_tweets, name='nba_tweets'),
    path('nba/tweets/<str:sport>', add_twitter_user, name='add_twitter_user'),
    path('mlb', mlb, name='mlb'),
    path('mlb/tweets', mlb_tweets, name='mlb_tweets'),
    path('mlb/tweets/<str:sport>', add_twitter_user, name='add_twitter_user'),
    path('mlb/<str:team_name>', mlb_team, name='mlb_team'),

    # path('mlb/tweets/<str:user>', views.add_twitter_user, name='add_twitter_user'),
    #path('get_teams/', views.get_teams, name='get_teams'),
]