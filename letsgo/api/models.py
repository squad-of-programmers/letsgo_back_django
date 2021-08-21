from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value
from django.db.models.fields import PositiveBigIntegerField


class Tour(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)


class Blogger(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephon = models.CharField(max_length=12) # for example: +7 345 678 90 12
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # social_networks 
    # 1
    # social_networks = models.JSONField(encoder=None, decoder=None, default=Value('null'))

    # 2
    # instagram = models.OneToOneField("main.InstagramAccount", on_delete=models.CASCADE)
    # facebook = models.OneToOneField("main.FacebookAccount", on_delete=models.CASCADE)
    # youtube = models.OneToOneField("main.InstagramAccount", on_delete=models.CASCADE)
    
    # 3

    count_success_tours = models.IntegerField()
    tours = models.ManyToManyField("api.Tour", related_name="blogger")


class SocialNetworkData(models.Model):
    network_title = models.ForeignKey("api.NetworkTitle", on_delete=models.CASCADE, null=False)
    blogger = models.ForeignKey("api.Blogger", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    link = models.URLField(max_length=255, null=True)
    num_subscribers = PositiveBigIntegerField(null=True)
    num_publications = PositiveBigIntegerField(null=True)


class NetworkTitle(models.Model):
    title = models.CharField(max_length=255)