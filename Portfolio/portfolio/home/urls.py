from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='About'),
    path('project', views.project, name='Project'),
    path('contact', views.contact, name='Contact')
]