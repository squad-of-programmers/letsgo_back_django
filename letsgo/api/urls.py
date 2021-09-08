from django.urls import path
from . import views


urlpatterns = [
    # ?from=0
    # &to=5 
    # &registered=True
    # &is_archive=True 
    # &name_contains=nikita
    # &gender='m'|'f'
    # &location='Ulyanovsk'
    # &age_gt=18
    # &age_lt=34
    # &tours_num_gt=2
    # &tours_num_lt=4
    # &tour_participant=3 # id of the tour 

    # &job='blogger'|'media' 
    # &in_tour=True
    # &is_invited=False
    # &get_tours=True
    # &get_social_networks=True
    path('bloggers', views.BloggerListAPI.as_view(), name='blogger_list'),
    path('bloggers/toggle_ban', views.ToggleBanAPI.as_view(), name='blogger_list'),
    path('bloggers/<slug:blogger_slug>',
        views.BloggerDetailAPI.as_view(), 
        name='blogger_detail'),

    # path('blogger_profiles/<slug:blogger_slug>', views.BloggerDetailAPI.as_view(), name='blogger_profile_detail'),

    path('tours', views.TourListAPI.as_view(), name='tour_list'),
    path('tours/<int:tour_slug>', views.TourDetailAPI.as_view(), name='tour_detail'),
]