from django.urls import path

from . import views

urlpatterns = [
    path('', views.cms_home, name='cms_home'),
    path('competitions/new/', views.new_competition, name='new_competition'),
    path('login/', views.login, name='login'),
    path('users/new/', views.new_user, name='new_user'),
]
