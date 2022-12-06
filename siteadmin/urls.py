from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_home, name='site_home'),
    path('countries/<abbreviation>/', views.country_details, name='country_details'),
    path('sports/<name>/', views.sport_details, name='sport_details'),
    path('users/new/', views.new_user, name='new_user'),
    path('users/<username>/', views.user_details, name='user_details'),
]
