from __future__ import print_function

from django.http import HttpResponseRedirect
from django.shortcuts import render
import mlbgame
import pandas
import nba_api
from nba_api.stats.static import teams
import nba_api.stats.endpoints as endpoints
import nba_api.stats.endpoints.leaguegamefinder as leaguegamefinder

from stats.models import Game

# Create your views here.
# def index(request):
#     return render(request, 'templates/stats/index.html')
from django.views import generic


def index(request):
    mlb_teams = mlbgame.teams()
    nba_teams = teams.get_teams()
    nba_teams = sorted(nba_teams, key=lambda  a: a['abbreviation'], reverse=False)
    context = {
        'mlb_teams': mlb_teams,
        'nba_teams': nba_teams
    }
    return render(request, 'stats/index.html', context)


def get_teams(request):
    print(get_teams.__name__)
    #mlb_teams = mlbgame.teams()
    # for team in mlb_teams:
    #     print(team)
    #     print(team.team_id)

    nba_teams = teams.get_teams()
    nba_teams = sorted(nba_teams, key=lambda  a: a['abbreviation'], reverse=False)
    #nba_teams = sorted(nba_teams)
    raptors_team_id = 1610612761
    nba_teams_games = []
    gamefinder = leaguegamefinder.LeagueGameFinder()
    games = gamefinder.get_data_frames()[0]
    games_1718 = games[games.SEASON_ID.str[-4:] == '2018']
    #games_1718 = games_1718.sort_values(by =['TEAM_ABBREVIATION'])
    for team in nba_teams:
        print(team)
        team_games_1718 = games_1718[games_1718.TEAM_ABBREVIATION == team['abbreviation']]
        team_games_1718_date = team_games_1718['GAME_DATE'][:5]
        team_games_1718_matchup = team_games_1718['MATCHUP'][:5]

        print("xxxxxxxxxxxxxxxxxxxxx")
        games = []
        for date,matchup in zip(team_games_1718_date, team_games_1718_matchup):
            matchup = matchup.replace(".", "")
            home_team = ""
            away_team = ""
            if 'vs' in matchup:
                home_team = matchup.split("vs")[0]
                away_team = matchup.split("vs")[1]
            elif '@' in matchup:
                away_team = matchup.split("@")[0]
                home_team = matchup.split("@")[1]

            away_team = away_team.strip()
            home_team = home_team.strip()
            print("%s %s vs %s" % (date, away_team, home_team))
            games.append(Game(date, away_team, home_team))
        print("xxxxxxxxxxxxxxxxxxxxx")
        print(list(games))

        nba_team_games = {'team_name': team['abbreviation'],
                          'team_games': games}
        nba_teams_games.append(nba_team_games)


    # teams.sort(key = lambda team: team.team_id)
    # #game = mlbgame.day(2019, 5, 28, home='Yankees')[0]
    # #game = mlbgame.day(2019, 5, 28, home='Yankees')[0]
    # month = mlbgame.games(2015, 6, home='Yankees')
    # print("Index Stats 1")
    # print(month)
    # #print(game.game_id)
    # #stats = mlbgame.player_stats(game.game_id)
    # #games = mlbgame.combine_games(month)
    # print("Index Stats 2")
    # # print(stats)
    # # for player in stats.home_batting:
    # #     print(player)

    # print("Index Stats 3")
    # # for game in games:
    # #     print(game)
    #
    # # for player in stats.home_batting:
    # #     print(player)

    # day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
    # game = day[0]
    # output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
    # print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))
    #
    # game = mlbgame.day(2015, 11, 1, home='Mets')[0]
    # stats = mlbgame.player_stats(game.game_id)
    # for player in stats.home_batting:
    #     print(player)

    context = {
        #'mlb_teams': mlb_teams,
        'nba_teams': nba_teams,
        'nba_teams_games': nba_teams_games
    }
    print("........................................")
    return render(request, 'stats/index.html', context)
# class IndexView(generic.ListView):
#     template_name = 'stats/index.html'
#     context_object_name = 'games'
#     month = mlbgame.games(2019, 6, home='Yankees')
#     games = mlbgame.combine_games(month)
# def get_queryset(self):
#     """Return the last five published questions."""
#     return Question.objects.order_by('-pub_date')[:5]
