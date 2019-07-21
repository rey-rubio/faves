from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
# class Game:
#
#     def __init__(self, game_id, date, away_team_name, home_team_name):
#         self.game_id = game_id
#         self.date = date
#         self.away_team_name = away_team_name
#         self.home_team_name = home_team_name
#
#     def __repr__(self):
#         return "%s %s @ %s" % (self.date, self.away_team_name, self.home_team_name)
#
#
# class Team:
#     def __init__(self, team_id, full_name, nickname, abbreviation, sport):
#         self.team_id = team_id
#         self.full_name = full_name
#         self.nickname = nickname
#         self.abbreviation = abbreviation
#         self.sport = sport
#         self.games = []
#
#     def set_games(self, games):
#         self.games = games
#     #
#     # def __str__(self):
#     #     return "%s (%s)" % (self.name, self.abbreviation)
#
#     def __repr__(self):
#         return "%s (%s)" % (self.full_name, self.abbreviation)


# class User(AbstractUser):
#     full_name = models.CharField(max_length=100, blank=False)
#     age = models.PositiveIntegerField(null=True, blank=True)

# NBA = "NBA"
# MLB = "MLB"
class Sport(models.Model):
    name = models.CharField(max_length=32, unique=True, null=True)
    abbreviation = models.CharField(max_length=3, unique=True, null=True)

    def __repr__(self):
        return "%s" % self.name


class Team(models.Model):
    team_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=32, unique=True, null=True)
    nickname = models.CharField(max_length=32, unique=True, null=True)
    abbreviation = models.CharField(max_length=3, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return "%s (%s)" % (self.full_name, self.abbreviation)
    def __str__(self):
        return "%s (%s)" % (self.full_name, self.abbreviation)

class Game(models.Model):
    game_id = models.IntegerField(null=True)
    home_team_name = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='home_team_name')
    away_team_name = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='away_team_name')
    date = models.DateTimeField(null=True)


class Player(models.Model):
    player_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)


TWITTER = "Twitter"
INSTAGRAM = "Instagram"
FACEBOOK = "Facebook"
class SocialMedia(models.Model):
    SOCIAL_MEDIA_TYPES = (
        (TWITTER, 'Twitter'),
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram')
    )
    sm_id = models.IntegerField(null=True)
    type = models.CharField(max_length=32, choices=SOCIAL_MEDIA_TYPES, null=True)
    name = models.CharField(max_length=32, null=True)
    handle = models.CharField(max_length=32, null=True)
