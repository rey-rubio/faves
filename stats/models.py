from django.db import models

# Create your models here.
class Game:

    def __init__(self, date, away_team, home_team):
        self.date = date
        self.away_team = away_team
        self.home_team = home_team

    def __str__(self):
        return "%s %s vs %s" % (self.date, self.home_team, self.away_team)

    def __repr__(self):
        return "%s %s vs %s" % (self.date, self.home_team, self.away_team)