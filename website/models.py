from django.db import models

# Create your models here.


class UserConnect(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


class OurTeams(models.Model):
    name = models.CharField(max_length=255)
    images = models.FileField(upload_to="")
    position = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)


class Services(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)


class AuwaveDetails(models.Model):
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    number = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)
