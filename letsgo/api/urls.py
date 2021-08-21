from django.urls import path
from . import views


urlpatterns = [
    path('bloggers', views.BloggerListAPI.as_view(), name='blogger_list'),
    path('bloggers/<int:blogger_id>', views.BloggerDetailAPI.as_view(), name='blogger_detail'),
    path('tours', views.TourListAPI.as_view(), name='tour_list'),
    path('tours/<int:tour_id>', views.TourDetailAPI.as_view(), name='tour_detail'),
]