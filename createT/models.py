from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (0, 'Simmetexon'),
      (1, 'Diorganotis'),
  )

  userType = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=0)



class Tournament(models.Model):

    Sports = 'Sports'
    eSports = 'eSports'
    Card_Games = 'Card_Games'

    TOURNAMENT_TYPE = (
        (Sports, 'Sports'),
        (eSports, 'e-Sports'),
        (Card_Games, 'Card Games'),
    )
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    dateStart = models.DateField(null=True)
    dateEnd = models.DateField(null=True)
    Tournament_Type = models.CharField(max_length=30, choices=TOURNAMENT_TYPE, default=Sports)
    location = models.CharField(max_length=200, null=True)
    regPrice = models.FloatField(null=True)
    Prize = models.FloatField(null=True)
    PpT = models.IntegerField(null=True)


    def __str__(self):
        return self.name

class Simmetoxi(models.Model):
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    tournament = models.ManyToManyField(Tournament)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    teamName = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.teamName
