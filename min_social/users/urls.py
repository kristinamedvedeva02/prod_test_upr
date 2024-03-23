from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('registration', views.registration, name = 'registration'),
    path('authentification', views.user_login , name = 'authentification'),
    path('profile', profile_pole, name = 'profile'),
]