from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_home, name='site_home'),
    path('countries/all/', views.all_countries, name='all_countries'),
    path('countries/new/', views.new_country, name='new_country'),
    path('countries/<abbreviation>/', views.country_details, name='country_details'),
    path('sports/new/', views.new_sport, name='new_sport'),
    path('sports/<name>/', views.sport_details, name='sport_details'),
    path('users/new/', views.new_user, name='new_user'),
    path('users/<username>/', views.user_details, name='user_details'),
]
