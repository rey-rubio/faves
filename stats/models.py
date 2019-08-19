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

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")

        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.active = True
        user.basic = False
        user.premium = False
        user.staff = False
        user.admin = False
        user.save(using=self._db)
        return user

    def create_basicuser(self, email, password):
        """
        Creates and saves a basic user with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.active = True
        user.basic = True
        user.premium = False
        user.staff = False
        user.admin = False
        user.save(using=self._db)
        return user

    def create_premiumuser(self, email, password):
        """
        Creates and saves a premium user with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.active = True
        user.basic = True
        user.premium = True
        user.staff = False
        user.admin = False
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.active = True
        user.basic = True
        user.premium = True
        user.staff = True
        user.admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a super user with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.active = True
        user.basic = True
        user.premium = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id         = models.AutoField(primary_key=True)
    email           = models.EmailField(max_length=255, unique=True)
    active          = models.BooleanField(default=True)     # if the user's account is active
    basic           = models.BooleanField(default=False)    # if the user has basic website privilleges
    premium         = models.BooleanField(default=False)    # if the user has premium website privilleges
    staff           = models.BooleanField(default=False)    # if the user has staff website privilleges
    admin           = models.BooleanField(default=False)    # if the user has admin website privilleges
    date_joined     = models.DateTimeField(auto_now_add=True, null=True)

    # replace built-in username field 
    USERNAME_FIELD  = 'email'

    # email and password are required by default
    REQUIRED_FIELDS = []
    
    # hook in the UserManager to custom User model
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_basic(self):
        "Does the user have basic website privilleges?"
        return self.basic

    @property
    def is_premium(self):
        "Does the user have premium website privilleges?"
        return self.premium

    @property
    def is_staff(self):
        "Does the user have staff website privilleges?"
        return self.staff    
    @property
    def is_admin(self):
        "Does the user have admin website privilleges?"
        return self.admin


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