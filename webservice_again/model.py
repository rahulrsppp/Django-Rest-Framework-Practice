import django
from django.db import models
from django import forms

from django.contrib.auth.models import AbstractBaseUser, UserManager


class Snippet(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(default="")
    mobile = models.IntegerField(default="")

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(default="", max_length=20)
    email = models.EmailField(default="")
    mobile = models.IntegerField(default="")
    username = models.CharField(default="",max_length=20)
    password = models.CharField(default="", max_length=20)

    def __str__(self):
        return self.name



class VoterList(models.Model):
    # id = models.IntegerField(auto_created= True, primary_key=True)
    name = models.CharField( max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    city = models.CharField( max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# class MyUser(AbstractBaseUser):
#     gender = models.CharField(default="M",max_length=6)

