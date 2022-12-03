from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_home, name='site_home'),
    path('users/new/', views.new_user, name='new_user'),
]
