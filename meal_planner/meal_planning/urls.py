"""Defines URL patterns for meal_planning"""

from django.urls import path

from . import views

app_name = 'meal_planning'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index')
]