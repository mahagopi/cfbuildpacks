from django.urls import path
from django.contrib.auth import views as auth_views

from allauth import account

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('login/', views.login, name='q'),
    path('signup/', views.signup, name='qq'),
    path('logout/', views.logout, name='qqq'),

]