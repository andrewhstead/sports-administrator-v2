from django.urls import path

from . import views

urlpatterns = [
    path('', views.cms_home, name='cms_home'),
    path('login/', views.login, name='login'),
]
