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

import mlbgame


def mlb(request):
    # mlb_teams = mlbgame.teams()
    context = {}
    context.update(get_mlb_teams())
    context.update(get_mlb_games_today())
    return render(request, 'faves/mlb.html', context)


def mlb_team(request, team_name):
    # mlb_teams = mlbgame.teams()
    print("TESTTTTTTTTTTTTTTTTT mlb_team: " + team_name)
    mlb_teams = get_mlb_teams()
    this_team = None
    for team in mlb_teams['mlb_teams']:
        if team.nickname.lower() == team_name:
            this_team = team
    print(this_team)
    context = {
        "team": this_team

    }
    return render(request, 'faves/mlb_team.html', context)


def get_mlb_teams():
    mlb = Sport.objects.filter(abbreviation="MLB").first()
    mlb_teams = Team.objects.filter(sport=mlb)

    print(mlb_teams)
    context = {
        'mlb_teams': mlb_teams
    }
    print("........................................")
    return context


def get_mlb_games_today():
    now = datetime.now()
    day = mlbgame.day(now.year, now.month, now.day)
    day.sort(key=lambda d: datetime.strptime(d.game_start_time, '%I:%M %p'), reverse=False)

    for game in day:
        print(game.game_id)
    # print(game.game_id)
    # test = mlbgame.box_score(game.game_id)
    # mlbgame.overview(game.game_id)
    # mlbgame.players(game.game_id)
    # mlbgame.team_stats(game.game_id)
    # mlbgame.player_stats(game.game_id)
    # mlbgame.game_events(game.game_id)

    print(day)
    context = {
        "games_today": day

    }
    return context


tweets_mlb = {}
tweets_mlb = set(tweets_mlb)
users_mlb = {"MLB", "Yankees", "mlbtraderumors", "Ken_Rosenthal", "JonHeymanCBS", "Buster_ESPN"}


def mlb_tweets(request):
    print(mlb_tweets.__name__)
    print(request)
    print(request.get_full_path())
    for user in users_mlb:
        data = TWITTER_API.GetUserTimeline(screen_name=user, count=5)

        for new_tweet in data:
            # print(new_tweet)
            # print(new_tweet.id)
            if not any(new_tweet.id == tweet.id for tweet in tweets_mlb):
                tweets_mlb.add(new_tweet)

    sorted_tweets_mlb = sorted(tweets_mlb, key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                               reverse=True)

    print(tweets_mlb)
    context = {
        'sport': "mlb",
        'tweets': sorted_tweets_mlb,
        'users': users_mlb
    }

    return render(request, 'faves/tweets.html', context)
