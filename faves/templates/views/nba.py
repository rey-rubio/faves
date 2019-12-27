from __future__ import print_function

import twitter
from django.shortcuts import render

from faves.models import Sport, Team
from myfaves.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_ACCESS_TOKEN_KEY, \
    TWITTER_CONSUMER_TOKEN_SECRET

TWITTER_API = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                          consumer_secret=TWITTER_CONSUMER_SECRET,
                          access_token_key=TWITTER_CONSUMER_ACCESS_TOKEN_KEY,
                          access_token_secret=TWITTER_CONSUMER_TOKEN_SECRET)

import datetime
from datetime import datetime


def nba(request):
    context = get_nba_teams()
    return render(request, 'faves/nba.html', context)


def get_nba_teams():
    nba = Sport.objects.filter(abbreviation="NBA").first()
    nba_teams = Team.objects.filter(sport=nba).order_by("abbreviation")
    print(nba_teams)
    context = {
        'nba_teams': nba_teams
    }
    return context


tweets_nba = {}
tweets_nba = set(tweets_nba)
users_nba = {"NBA", "wojespn", "ShamsCharania", "ZachLowe_NBA", "sam_amick", "TheSteinLine", "ChrisBHaynes",
             "davidaldridgedc", "WindhorstESPN"}


def nba_tweets(request):
    print(nba_tweets.__name__)
    print(request)
    print(request.get_full_path())
    for user in users_nba:
        data = TWITTER_API.GetUserTimeline(screen_name=user, count=5)

        for new_tweet in data:
            # print(new_tweet)
            # print(new_tweet.id)
            if not any(new_tweet.id == tweet.id for tweet in tweets_nba):
                tweets_nba.add(new_tweet)

    sorted_tweets_nba = sorted(tweets_nba, key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                               reverse=True)

    print(tweets_nba)
    context = {
        'sport': "nba",
        'tweets': sorted_tweets_nba,
        'users': users_nba
    }

    return render(request, 'faves/tweets.html', context)
