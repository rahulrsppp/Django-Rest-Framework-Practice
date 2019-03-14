import django
from django.db import models
from django import forms

from django.contrib.auth.models import AbstractBaseUser, UserManager, User


class Snippet(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(default="")
    mobile = models.IntegerField(default="") # default should be 0

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(default="", max_length=20)
    email = models.EmailField(default="") 
    mobile = models.IntegerField(default="") # default should be 0
    username = models.CharField(default="",max_length=20)
    password = models.CharField(default="", max_length=20)

    def __str__(self):
        return self.name



class VoterList(models.Model):
    name = models.CharField(default="", max_length=20)
    email = models.EmailField(default="")
    mobile = models.IntegerField(default="")
    city = models.CharField(default="", max_length=20)
    type = models.CharField(default="",max_length=20)

    def __str__(self):
        return self.name
