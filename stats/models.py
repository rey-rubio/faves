from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
# from django.contrib.auth.models import AbstractUser
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


# class StuffHubUser(AbstractUser):
#     full_name = models.CharField(max_length=100, blank=False)
#     age = models.PositiveIntegerField(null=True, blank=True)

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, active=True, basic=False, admin=False):
#         if not email:
#             raise ValueError("Users must have an email address.")
#         if not password:
#             raise ValueError("Users must have a password.")
#         user = self.model(
#             email = self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.active = active
#         user.basic = basic
#         user.admin = admin
#         user.save(using=self._db)
#         return user

#     def create_basic_user(self, email, password=None):
#         user = self.create_user(
#                     email,
#                     password=password,
#                     basic=True)
#         return user

#     def create_super_user(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             basic=True,
#             admin=True)
#         return user

# class User(AbstractBaseUser):
#     user_id         = models.AutoField(primary_key=True)
#     email           = models.EmailField(max_length=255, unique=True, null=True)
#     # first_name      = models.CharField(max_length=255, blank=True, null=True)
#     # last_name       = models.CharField(max_length=255, blank=True, null=True)
#     active          = models.BooleanField(default=True, null=True)
#     basic           = models.BooleanField(default=True, null=True)
#     admin           = models.BooleanField(default=True, null=True)
#     date_joined     = models.DateTimeField(auto_now_add=True, null=True)

#     USERNAME_FIELD  = 'email'
#     # email and password are required by default
#     REQUIRED_FIELDS = []
#     objects = UserManager()
#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.email

#     def get_short_name(self):
#         return self.email

#     @property
#     def is_active(self):
#         return self.active

#     @property
#     def is_basic(self):
#         return self.basic
#     @property
#     def is_admin(self):
#         return self.admin

# NBA = "NBA"
# MLB = "MLB"
class Sport(models.Model):
    api_id              = models.IntegerField(unique=True, null=True)
    name                = models.CharField(max_length=50, unique=True, null=True)
    abbreviation        = models.CharField(max_length=3, unique=True, null=True)

    def __repr__(self):
        return "%s" % self.name

    def __str__(self):
        return "%s" % self.name


class Team(models.Model):
    api_id              = models.IntegerField(unique=True, null=True)
    full_name           = models.CharField(max_length=50, unique=True, null=True)
    nickname            = models.CharField(max_length=50, unique=True, null=True)
    abbreviation        = models.CharField(max_length=3, null=True)
    sport               = models.ForeignKey(Sport, null=True, on_delete=models.CASCADE)

    def __repr__(self):
        return "%s (%s)" % (self.full_name, self.abbreviation)

    def __str__(self):
        return "%s (%s)" % (self.full_name, self.abbreviation)

class Game(models.Model):
    api_id              = models.IntegerField(unique=True, null=True)
    home_team_id        = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='home_team_id')
    away_team_id        = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='away_team_id')
    date                = models.DateTimeField(null=True)

#test
class Player(models.Model):
    api_id              = models.IntegerField(unique=True, null=True)
    first_name          = models.CharField(max_length=50, null=True)
    last_name           = models.CharField(max_length=50, null=True)
    team                = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

class Influencer(models.Model):
    first_name          = models.CharField(max_length=50, null=True)
    last_name           = models.CharField(max_length=50, null=True)
    nickname            = models.CharField(max_length=50, null=True)

class SocialMedia(models.Model):
    influencer          = models.ForeignKey(Influencer, on_delete=models.CASCADE, null=True)

class Twitter(models.Model):
    social_media        = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, null=True)
    api_id              = models.IntegerField(unique=True, null=True)
    handle              = models.CharField(max_length=50, null=True)

class Facebook(models.Model):
    social_media        = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, null=True)
    api_id              = models.IntegerField(unique=True, null=True)
    handle              = models.CharField(max_length=50, null=True)

class Instagram(models.Model):
    social_media        = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, null=True)
    api_id              = models.IntegerField(unique=True, null=True)
    handle              = models.CharField(max_length=50, null=True)