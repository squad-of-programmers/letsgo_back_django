from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value
from django.db.models.fields import DateTimeField, PositiveBigIntegerField
from django.contrib.auth.models import User, UserManager
from django.template.defaultfilters import slugify
from django.urls import reverse

"""
TODO:
* models for report_blogger_materials
* models for chat 'Blogger <-> Admin'

"""


GENDER_CHOICES = (
    ('m', 'male'),
    ('f', 'female'),
)


class Job(models.Model):
    """
    kind of activity
    'b': 'blogger' 
    'm': 'media' - in Russian: СМИ
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)


class Tour(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    
    points = models.JSONField(default=dict)


    def get_absolute_url(self):
        return reverse('tour_detail', kwargs={'tour_slug': self.slug}) # new

    class Meta:
        verbose_name = 'Tour'


# class BloggerProfile(models.Model):
#     """
#     username - in the user object
#     last_name - in the user object

#     Registered bloggers.
#     """

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
#     slug = models.SlugField(null=False, unique=True)

#     avatar = models.ImageField(upload_to='media/avatars', height_field='600', width_field='400')
#     # think about image sizes!
#     telephone = models.CharField(max_length=12) # for example: +7 345 678 90 12
#     location = models.CharField(max_length=255)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

#     is_archive = models.BooleanField(default=False)

#     job = models.ForeignKey("api.Job", on_delete=models.SET_NULL, null=True)
#     tours = models.ManyToManyField("api.Tour", related_name="blogger")

    
#     def get_absolute_url(self):
#         return reverse('blogger_profile_detail', kwargs={'blogger_slug': self.slug}) # new
    


class Blogger(models.Model):
    """
    You can select some and send them an invitation to the event with a registration link.

    Можно отобрать некоторых и отправить им приглашение на мероприятие с ссылкой на регистрацию.
    """

    # pk if blogger is regestered else null
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='blogger_profile', null=True)

    slug = models.SlugField(unique=True, null=False)
    username = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    avatar_xl = models.ImageField(upload_to='media/avatars/xl', height_field='500', width_field='400', null=True)
    avatar_lg = models.ImageField(upload_to='media/avatars/lg', height_field='100', width_field='100', null=True)
    avatar_sm = models.ImageField(upload_to='media/avatars/sm', height_field='32', width_field='32', null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_archive = models.BooleanField(default=False)

    telephone = models.CharField(max_length=12, null=True) # for example: +7 345 678 90 12
    location = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(null=True)

    job = models.ForeignKey('api.Job', related_name='bloggers', on_delete=models.SET_NULL, null=True)

    count_success_tours = models.IntegerField()
    tours = models.ManyToManyField('api.Tour', related_name='bloggers', through='api.BloggerTour')
    
    # social_networks 
    # 1 [ ]
    # todo: make encoder and decoder for social_networks
    # {
    #   {
    #       'title': 'facebook',
    #       'username': 'nikita',
    #       'link': 'https://facebook.com/nikita99',
    #       'num_subscribers': 99,
    #       'num_publications': 45,
    #       'publications_per_month': 18,
    #       'subscribers_per_month': 11, 
    #   }
    # } 
    social_networks = models.JSONField(default=dict)


    def __str__(self):
        return self.get_name()

    def get_absolute_url(self):
        return reverse('blogger_detail', kwargs={'blogger_slug': self.slug})
    
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.get_name())
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Blogger'


INVITATION_STATUS_CHOICES = (
    ('i', 'invited'),
    ('a', 'accepted'),
    ('r', 'regected')
)


class BloggerTour(models.Model):
    blogger = models.ForeignKey('api.Blogger', on_delete=models.CASCADE)
    tour = models.ForeignKey('api.Tour', on_delete=models.CASCADE)

    date_joined = models.DateField(null=True)
    date_invited = models.DateField(null=True)

    invitation_status = models.CharField(max_length=1, choices=INVITATION_STATUS_CHOICES, default='i')
    was_skipped = models.BooleanField() # Ether the blogger visited or skipped the tour


# ????????
# class SocialNetworkData(models.Model):
#     network_title = models.ForeignKey("api.NetworkTitle", on_delete=models.CASCADE, null=False)
#     blogger = models.ForeignKey("api.Blogger", on_delete=models.CASCADE)
#     username = models.CharField(max_length=255)
#     link = models.URLField(max_length=255, null=True)
#     num_subscribers = PositiveBigIntegerField(null=True)
#     num_publications = PositiveBigIntegerField(null=True)

#     class Meta:
#         verbose_name = "Social network data"


# class NetworkTitle(models.Model):
#     title = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = "Network title"