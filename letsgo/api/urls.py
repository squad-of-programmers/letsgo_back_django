from django.urls import path
from . import views


urlpatterns = [
    path('bloggers', views.BloggerListAPI.as_view(), name='blogger_list'),
    path('bloggers/<slug:blogger_slug>', views.BloggerDetailAPI.as_view(), name='blogger_detail'),

    path('bloggers', views.BloggerListAPI.as_view(), name='blogger_prifile_list'),
    path('blogger_profiles/<slug:blogger_slug>', views.BloggerDetailAPI.as_view(), name='blogger_profile_detail'),

    path('tours', views.TourListAPI.as_view(), name='tour_list'),
    path('tours/<int:tour_slug>', views.TourDetailAPI.as_view(), name='tour_detail'),
]