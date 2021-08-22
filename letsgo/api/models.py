from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value
from django.db.models.fields import DateTimeField, PositiveBigIntegerField
from django.contrib.auth.models import User, UserManager
from django.template.defaultfilters import slugify
from django.urls import reverse


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

# ACTIVITY_CHOICES = (
#     ('B', 'Blogger'), 
#     ('M', 'Media') # in Russian: СМИ
# )


class Job(models.Model):
    """
    kind of activity
    """
    title = models.CharField(max_length=255)


class Tour(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    points = models.JSONField(null=True)

    def get_absolute_url(self):
        return reverse('tour_detail', kwargs={'tour_slug': self.slug}) # new

    class Meta:
        verbose_name = "Tour"


class BloggerProfile(models.Model):
    """
    username - in the user object
    last_name - in the user object

    Registered bloggers.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    slug = models.SlugField(null=False, unique=True)

    avatar = models.ImageField(upload_to='media/avatars', height_field='600', width_field='400')
    # think about image sizes!
    telephone = models.CharField(max_length=12) # for example: +7 345 678 90 12
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    is_archive = models.BooleanField(default=False)

    job = models.ForeignKey("api.Job", on_delete=models.SET_NULL, null=True)
    # kind_of_activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
    
    def get_absolute_url(self):
        return reverse('blogger_profile_detail', kwargs={'blogger_slug': self.slug}) # new

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Registered blogger"


class Blogger(models.Model):
    """
    Those bloggers that were found using algorithms on different social networks.
    You can select some and send them an invitation to the event with a registration link.

    Те блогеры, что были найдены с помощью алгоритмов на разных соцсетях.
    Можно отобрать некоторых и отправить им приглашение на мероприятие с ссылкой регистрацию.
    """

    slug = models.SlugField(null=False, unique=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    is_archive = models.BooleanField(default=False)

    telephone = models.CharField(max_length=12) # for example: +7 345 678 90 12
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    job = models.ForeignKey("api.Job", on_delete=models.SET_NULL, null=True)

    count_success_tours = models.IntegerField()
    tours = models.ManyToManyField("api.Tour", related_name="blogger")
    
    # social_networks 
    # 1 [ ]
    # social_networks = models.JSONField(encoder=None, decoder=None, default=Value('null'))

    # 2 [ ]
    # instagram = models.OneToOneField("main.InstagramAccount", on_delete=models.CASCADE)
    # facebook = models.OneToOneField("main.FacebookAccount", on_delete=models.CASCADE)
    # youtube = models.OneToOneField("main.InstagramAccount", on_delete=models.CASCADE)
    
    # 3 [x]
    # look at blogger field in SocialNetworkData 


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogger_detail', kwargs={'blogger_slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Blogger"


class SocialNetworkData(models.Model):
    network_title = models.ForeignKey("api.NetworkTitle", on_delete=models.CASCADE, null=False)
    blogger = models.ForeignKey("api.Blogger", on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    link = models.URLField(max_length=255, null=True)
    num_subscribers = PositiveBigIntegerField(null=True)
    num_publications = PositiveBigIntegerField(null=True)

    class Meta:
        verbose_name = "Social network data"


class NetworkTitle(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Network title"