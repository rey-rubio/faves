from __future__ import print_function
from mysite.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_ACCESS_TOKEN_KEY,TWITTER_CONSUMER_TOKEN_SECRET
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import mlbgame

import nba_api.stats.endpoints.leaguegamefinder as leaguegamefinder
from nba_api.stats.static import teams

import twitter
from stats.models import Game, Team

import datetime
from datetime import datetime
api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_CONSUMER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_CONSUMER_TOKEN_SECRET)

def index(request):
    # mlb_teams = mlbgame.teams()
    # context = get_teams()

    return render(request, 'stats/index.html', )

#################################################################
#################################################################
#################################################################

def nba(request):
    # mlb_teams = mlbgame.teams()
    context = get_nba_teams()
    return render(request, 'stats/nba.html', context)


def get_nba_teams():
    nba_teams_data = teams.get_teams()
    nba_teams_data = sorted(nba_teams_data, key=lambda a: a['abbreviation'], reverse=False)
    gamefinder = leaguegamefinder.LeagueGameFinder()
    games = gamefinder.get_data_frames()[0]
    games_1718 = games[games.SEASON_ID.str[-4:] == '2018']
    nba_teams = []
    for team in nba_teams_data:
        print(team)
        # Get columns from NBA API
        team_games_1718 = games_1718[games_1718.TEAM_ABBREVIATION == team['abbreviation']]
        team_games_1718_game_id = team_games_1718['GAME_ID'][:5]
        team_games_1718_date = team_games_1718['GAME_DATE'][:5]
        team_games_1718_matchup = team_games_1718['MATCHUP'][:5]

        # Iterate through dates and matchup to create Games objects
        games = []
        for game_id, date, matchup in zip(team_games_1718_game_id, team_games_1718_date, team_games_1718_matchup):
            matchup = matchup.replace(".", "")
            home_team_name = ""
            away_team_name = ""
            if 'vs' in matchup:
                away_team_name = matchup.split("vs")[1]
                home_team_name = matchup.split("vs")[0]
            elif '@' in matchup:
                away_team_name = matchup.split("@")[0]
                home_team_name = matchup.split("@")[1]

            away_team_name = away_team_name.strip()
            home_team_name = home_team_name.strip()
            # print("%s %s vs %s" % (date, away_team_name, home_team_name))
            games.append(Game(game_id, date, away_team_name, home_team_name))

        print(list(games))

        # Create Team object
        team_test = Team(team['id'], team['full_name'], team['nickname'], team['abbreviation'], "NBA")
        team_test.set_games(games)
        # Append to array of Teams
        nba_teams.append(team_test)

    print(nba_teams)
    context = {
        'nba_teams': nba_teams

    }
    print("........................................")
    # return render(request, 'stats/index.html', context)
    return context


def nba_tweets(request):
    print(api.VerifyCredentials())
    users = ["wojespn", "ShamsCharania", "ZachLowe_NBA", "sam_amick",
             "TheSteinLine", "ChrisBHaynes", "davidaldridgedc", "WindhorstESPN"]
    tweets = []
    for user in users:
        tweets.extend(api.GetUserTimeline(screen_name=user, count=5))
        tweets.sort(key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'), reverse = True)

    print(tweets)
    context = {
        'tweets': tweets,
        'users': users
    }

    return render(request, 'stats/tweets.html', context )

#################################################################
#################################################################
#################################################################

def mlb(request):
    # mlb_teams = mlbgame.teams()
    context = {}
    context.update(get_mlb_teams())
    context.update(get_mlb_games_today())
    return render(request, 'stats/mlb.html', context)


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
    return render(request, 'stats/mlb_team.html', context)


def get_mlb_games_today():
    now = datetime.now()
    day = mlbgame.day(now.year, now.month, now.day)
    day.sort(key=lambda d: datetime.strptime(d.game_start_time, '%I:%M %p'), reverse=False)

    for game in day:
        print(game.game_id)
    # print(game.game_id)
        #test = mlbgame.box_score(game.game_id)
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


def get_mlb_teams():
    # print(get_mlb_teams.__name__)
    mlb_teams_data = mlbgame.teams()

    mlb_teams = []
    for team in mlb_teams_data:
        # print(team)
        # print(team.team_id)

        team_test = Team(team.team_id, team.club_full_name, team.aws_club_slug, team.display_code.upper(), "MLB")
        mlb_teams.append(team_test)

    # game = mlbgame.day(2019, 5, 28, home='Yankees')[0]
    # game = mlbgame.day(2019, 5, 28, home='Yankees')[0]
    # month = mlbgame.games(2015, 6, home='Yankees')
    # print("Index Stats 1")
    # print(month)
    # print(game.game_id)
    # stats = mlbgame.player_stats(game.game_id)
    # games = mlbgame.combine_games(month)
    # print("Index Stats 2")
    # # print(stats)
    # # for player in stats.home_batting:
    # #     print(player)
    #
    # print("Index Stats 3")
    # # for game in games:
    # #     print(game)
    #
    # # for player in stats.home_batting:
    # #     print(player)
    #
    # day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
    # game = day[0]
    # output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
    # print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))
    #
    # game = mlbgame.day(2015, 11, 1, home='Mets')[0]
    # stats = mlbgame.player_stats(game.game_id)
    # for player in stats.home_batting:
    #     print(player)
    print(mlb_teams)
    context = {
        'mlb_teams': mlb_teams
    }
    return context


tweets = []
users = {"MLB"}

def mlb_tweets(request):

    # print(api.VerifyCredentials())

    for user in users:
        tweets.extend(api.GetUserTimeline(screen_name=user, count=5))

    tweets.sort(key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'), reverse=True)

    print(tweets)
    context = {
        'tweets': tweets,
        'users': users
    }

    return render(request, 'stats/tweets.html', context )
# class IndexView(generic.ListView):
#     template_name = 'stats/index.html'
#     context_object_name = 'games'
#     month = mlbgame.games(2019, 6, home='Yankees')
#     games = mlbgame.combine_games(month)
# def get_queryset(self):
#     """Return the last five published questions."""
#     return Question.objects.order_by('-pub_date')[:5]


def add_twitter_user(request):
    print(add_twitter_user.__name__)
    # try:
    #     #selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                      consumer_secret=TWITTER_CONSUMER_SECRET,
                      access_token_key=TWITTER_CONSUMER_ACCESS_TOKEN_KEY,
                      access_token_secret=TWITTER_CONSUMER_TOKEN_SECRET)
    if request.method == 'POST':
        user = request.POST.get('add_twitter_user', None)
        print(user)
        users.add(user)
        print(users)
        try:
            print(api.VerifyCredentials())
            # data = api.GetUserTimeline(screen_name=user, count=5)
            tweets.extend(api.GetUserTimeline(screen_name=user, count=5))
        except Exception as err:
            #return HttpResponseRedirect(reverse('stats:mlb_tweets'))
            print(err.message)
            for i in err.message:
                print(i)

        # print(request.POST['user'])
    return HttpResponseRedirect(reverse('stats:mlb_tweets'))
