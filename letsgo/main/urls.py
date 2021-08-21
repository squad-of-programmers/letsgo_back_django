from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('bloggers', views.BloggerAPIView.as_view(), name='bloggers'),
]