from django.db import models

# Create your models here.
class Game:

    def __init__(self, game_id, date, away_team_name, home_team_name):
        self.game_id = game_id
        self.date = date
        self.away_team_name = away_team_name
        self.home_team_name = home_team_name

    def __repr__(self):
        return "%s %s @ %s" % (self.date, self.away_team_name, self.home_team_name)


class Team:
    def __init__(self, team_id, full_name, nickname, abbreviation):
        self.team_id = team_id
        self.full_name = full_name
        self.nickname = nickname
        self.abbreviation = abbreviation
        self.abbreviation = abbreviation
        self.games = []

    def set_games(self, games):
        self.games = games
    #
    # def __str__(self):
    #     return "%s (%s)" % (self.name, self.abbreviation)

    def __repr__(self):
        return "%s (%s)" % (self.full_name, self.abbreviation)

