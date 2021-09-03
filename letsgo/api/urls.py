from django.urls import path
from . import views


urlpatterns = [
    #?start=0
    # &end=5 
    # &registered=True
    # &name_contains=nikita
    # &age_below=34
    # &age_above=18
    # &gender='m'|'f'
    # &job='blogger'|'media' #
    # &location='Ulyanovsk'
    # &tours_num_above=2
    # &tours_num_below=4
    # &in_tour=True
    # &is_invited=False
    # &is
    path('bloggers', views.BloggerListAPI.as_view(), name='blogger_list'),

    # path('bloggers/registered', views.BloggerListAPI.as_view(), name='blogger_prifile_list'),
    path('bloggers/<slug:blogger_slug>', views.BloggerDetailAPI.as_view(), name='blogger_detail'),

    # path('blogger_profiles/<slug:blogger_slug>', views.BloggerDetailAPI.as_view(), name='blogger_profile_detail'),

    path('tours', views.TourListAPI.as_view(), name='tour_list'),
    path('tours/<int:tour_slug>', views.TourDetailAPI.as_view(), name='tour_detail'),
]