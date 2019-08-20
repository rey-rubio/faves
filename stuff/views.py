from __future__ import print_function

import datetime
from datetime import datetime

import mlbgame
import twitter
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from stuff.models import Sport, Team, Influencer, SocialMedia, Twitter, Instagram, Youtube, Facebook
from stuffhub.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_ACCESS_TOKEN_KEY, \
    TWITTER_CONSUMER_TOKEN_SECRET

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_CONSUMER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_CONSUMER_TOKEN_SECRET)

def login(request):
    print(login.__name__)
    print(request)
    print(request.get_full_path())
    if request.method == 'POST':
        try:
            user = authenticate(email=request.POST.get('email', None), password=request.POST.get('password', None))
            if user is not None:
                login_user(request, user)
                return HttpResponseRedirect(reverse('stuff:index'))
            else:
                return HttpResponseRedirect(reverse('stuff:login_view'))

        except Exception as err:
            print(err.message)
            for i in err.message:
                print(i)

    return render(request, 'stuff/login.html')


# def login_user(request):


def register(request):
    return render(request, 'stuff/register.html')


def logout(request):
    logout_user(request)
    return render(request, 'stuff/login.html')


def index(request):
    print(index.__name__)
    print(request)
    print(request.get_full_path())
    if not request.user.is_authenticated:
        return render(request, 'stuff/login.html')

    return render(request, 'stuff/index.html')


def influencers(request):
    context = get_influencers()
    return render(request, 'stuff/influencers.html', context)


def get_influencers():
    entertainment = get_influencers_helper('Entertainment')
    fashion = get_influencers_helper('Fashion')
    food = get_influencers_helper('Food')
    gaming = get_influencers_helper('Gaming')
    makeup = get_influencers_helper('Makeup')
    sports_fitness = get_influencers_helper('Sports/Fitness')
    travel = get_influencers_helper('Travel')
    vlogging = get_influencers_helper('Vlogging')

    influencers = {
        'entertainment': entertainment,
        'fashion': fashion,
        'food': food,
        'gaming': gaming,
        'makeup': makeup,
        'sports_fitness': sports_fitness,
        'travel': travel,
        'vlogging': vlogging
    }

    # for industry in influencers:
    #     for influencer in industry:
    #         # print(influencer)

    # influencers = Influencer.objects.filter()
    # mlb_teams = Team.objects.filter(sport=mlb)

    # print(influencers)
    # context = {
    #     'influencers': influencers
    # }
    print("........................................")
    return influencers


def get_influencers_helper(industry):
    print(industry)
    # get influencers from a particular industry
    influencers = Influencer.objects.filter(industry=industry).order_by("level")

    influencers_map = []
    for influencer in influencers:
        print("influencer ........................................")
        print(influencer)
        print("social_media_id ........................................")
        # get social_media_id of particular influencer
        social_media_id = SocialMedia.objects.filter(influencer=influencer).first()
        print(social_media_id)

        influencer_map = {
            'id': influencer.id,
            'first_name': influencer.first_name,
            'last_name': influencer.last_name,
            'nickname': influencer.nickname,
            'level': influencer.level,
            'industry': influencer.industry,
            'twitter': '',
            'instagram': '',
            'youtube': '',
            'facebook': ''
        }
        print("twitter ........................................")
        # get all social medias using social_media id
        twitter = Twitter.objects.filter(social_media=social_media_id.id).order_by("id").first()
        print(twitter)
        print(twitter.handle)

        if twitter is not None:
            influencer_map.update({'twitter': twitter.handle})

        print("instagram ........................................")
        instagram = Instagram.objects.filter(social_media=social_media_id.id).order_by("id").first()
        print(instagram)
        if instagram is not None:
            influencer_map.update({'instagram': instagram.handle})

        print("youtube ........................................")
        youtube = Youtube.objects.filter(social_media=social_media_id.id).order_by("id").first()
        print(youtube)
        if youtube is not None:
            influencer_map.update({'youtube': youtube.handle})

        print("facebook  ........................................")
        facebook = Facebook.objects.filter(social_media=social_media_id.id).order_by("id").first()
        print(facebook)
        if facebook is not None:
            influencer_map.update({'facebook': facebook.handle})

        print("........................................")

        influencers_map.append(influencer_map)

    return influencers_map
#################################################################
#################################################################
#################################################################

def nba(request):
    # mlb_teams = mlbgame.teams()
    context = get_nba_teams()
    return render(request, 'stuff/nba.html', context)


def get_nba_teams():
    # nba_teams_data = teams.get_teams()
    # nba_teams_data = sorted(nba_teams_data, key=lambda a: a['abbreviation'], reverse=False)
    # gamefinder = leaguegamefinder.LeagueGameFinder()
    # games = gamefinder.get_data_frames()[0]
    # games_1718 = games[games.SEASON_ID.str[-4:] == '2018']
    # nba_teams = []
    # for team in nba_teams_data:
    #     # print(team)
    #     # Get columns from NBA API
    #     team_games_1718 = games_1718[games_1718.TEAM_ABBREVIATION == team['abbreviation']]
    #     team_games_1718_game_id = team_games_1718['GAME_ID'][:5]
    #     team_games_1718_date = team_games_1718['GAME_DATE'][:5]
    #     team_games_1718_matchup = team_games_1718['MATCHUP'][:5]
    #
    #     # Iterate through dates and matchup to create Games objects
    #     games = []
    #     for game_id, date, matchup in zip(team_games_1718_game_id, team_games_1718_date, team_games_1718_matchup):
    #         matchup = matchup.replace(".", "")
    #         home_team_name = ""
    #         away_team_name = ""
    #         if 'vs' in matchup:
    #             away_team_name = matchup.split("vs")[1]
    #             home_team_name = matchup.split("vs")[0]
    #         elif '@' in matchup:
    #             away_team_name = matchup.split("@")[0]
    #             home_team_name = matchup.split("@")[1]
    #
    #         away_team_name = away_team_name.strip()
    #         home_team_name = home_team_name.strip()
    #         # print("%s %s vs %s" % (date, away_team_name, home_team_name))
    #         games.append(Game(game_id, date, away_team_name, home_team_name))
    #
    #     # print(list(games))
    #
    #     # Create Team object
    #     team_test = Team(team['id'], team['full_name'], team['nickname'], team['abbreviation'], "NBA")
    #     # team_test.set_games(games) #####################################
    #     print("%s = Team(team_id=%s,full_name='%s',nickname='%s',abbreviation='%s',sport=%s)" % (
    #         team['abbreviation'], team['id'], team['full_name'], team['nickname'], team['abbreviation'],"NBA"))
    #     print("%s.save()" % (team['abbreviation']))
    #     # Append to array of Teams
    #     nba_teams.append(team_test)

    nba = Sport.objects.filter(abbreviation="NBA").first()
    nba_teams = Team.objects.filter(sport=nba).order_by("abbreviation")
    print(nba_teams)
    context = {
        'nba_teams': nba_teams

    }
    print("........................................")
    # return render(request, 'stuff/index.html', context)
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
        data = api.GetUserTimeline(screen_name=user, count=5)

        for new_tweet in data:
            # print(new_tweet)
            # print(new_tweet.id)
            if not any(new_tweet.id == tweet.id for tweet in tweets_nba):
                tweets_nba.add(new_tweet)

    sorted_tweets_nba = sorted(tweets_nba, key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                               reverse=True)

    print(tweets_mlb)
    context = {
        'sport': "nba",
        'tweets': sorted_tweets_nba,
        'users': users_nba
    }

    return render(request, 'stuff/tweets.html', context)


#################################################################
#################################################################
#################################################################

def mlb(request):
    # mlb_teams = mlbgame.teams()
    context = {}
    context.update(get_mlb_teams())
    context.update(get_mlb_games_today())
    return render(request, 'stuff/mlb.html', context)


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
    return render(request, 'stuff/mlb_team.html', context)


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


def get_mlb_teams():
    # print(get_mlb_teams.__name__)
    # mlb_teams_data = mlbgame.teams()
    #
    # mlb_teams = []
    # for team in mlb_teams_data:
    #     # print(team.team_id)
    #
    #     team_test = Team(team.team_id, team.club_full_name, team.aws_club_slug, team.display_code.upper(), "MLB")
    #     mlb_teams.append(team_test)
    # print("%s = Team(team_id=%s,full_name='%s',nickname='%s',abbreviation='%s',sport='%s')" % (team.display_code.upper(), team.team_id, team.club_full_name, team.aws_club_slug, team.display_code.upper(), "MLB"))
    # print("%s.save()" % (team.display_code.upper()))

    # game = mlbgame.day(2019, 5, 28, home='Yankees')[0]
    # game = mlbgame.day(2019, 5, 28, home='Yankees')[0]
    # month = mlbgame.games(2015, 6, home='Yankees')
    # print("Index Stats 1")
    # print(month)
    # print(game.game_id)
    # stuff = mlbgame.player_stats(game.game_id)
    # games = mlbgame.combine_games(month)
    # print("Index Stats 2")
    # # print(stuff)
    # # for player in stuff.home_batting:
    # #     print(player)
    #
    # print("Index Stats 3")
    # # for game in games:
    # #     print(game)
    #
    # # for player in stuff.home_batting:
    # #     print(player)
    #
    # day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
    # game = day[0]
    # output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
    # print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))
    #
    # game = mlbgame.day(2015, 11, 1, home='Mets')[0]
    # stuff = mlbgame.player_stats(game.game_id)
    # for player in stuff.home_batting:
    #     print(player)
    mlb = Sport.objects.filter(abbreviation="MLB").first()
    mlb_teams = Team.objects.filter(sport=mlb)

    print(mlb_teams)
    context = {
        'mlb_teams': mlb_teams
    }
    print("........................................")
    return context


tweets_mlb = {}
tweets_mlb = set(tweets_mlb)
users_mlb = {"MLB", "Yankees", "JeffPassan", "mlbtraderumors", "Ken_Rosenthal", "JonHeymanCBS", "Buster_ESPN"}
def mlb_tweets(request):
    print(mlb_tweets.__name__)
    print(request)
    print(request.get_full_path())
    for user in users_mlb:
        data = api.GetUserTimeline(screen_name=user, count=5)

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

    return render(request, 'stuff/tweets.html', context)


def add_twitter_user(request, sport):
    print(add_twitter_user.__name__)
    print(request)
    print(request.get_full_path())
    print(sport)
    if request.method == 'POST':
        user = request.POST.get('add_twitter_user', None)
        print(user)
        # print(users_nba)
        # messages.info(request, 'Successfully added user' + user)
        try:
            data = api.GetUserTimeline(screen_name=user, count=5)
            # print(new_tweet)
            # print(new_tweet.id)
            if (sport.lower() == "nba"):
                print("nba!!!")
                for new_tweet in data:
                    users_nba.add(user)
                    if not any(new_tweet.id == tweet.id for tweet in tweets_nba):
                        tweets_nba.add(new_tweet)

                # sorted_tweets_nba = sorted(tweets_nba,
                #                            key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                #                            reverse=True)
                return HttpResponseRedirect(reverse('stuff:nba_tweets'))

            elif (sport.lower() == "mlb"):
                print("mlb!!!")
                for new_tweet in data:
                    users_mlb.add(user)
                    if not any(new_tweet.id == tweet.id for tweet in tweets_mlb):
                        tweets_mlb.add(new_tweet)

                # sorted_tweets_mlb = sorted(tweets_mlb,
                #                            key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                #                            reverse=True)
                return HttpResponseRedirect(reverse('stuff:mlb_tweets'))

        except Exception as err:
            print(err.message)
            for i in err.message:
                print(i)

        # print(request.POST['user'])
    # if ("nba" in request.get_full_path()):
    #     return HttpResponseRedirect(reverse('stuff:nba_tweets'))
    # elif ("mlb" in request.get_full_path()):
    #     return HttpResponseRedirect(reverse('stuff:mlb_tweets'))
    # else:
    #     return HttpResponseRedirect(reverse('stuff:nba_tweets'))
