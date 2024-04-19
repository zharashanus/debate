from django.contrib import admin
from django.urls import path, include


# На это:
from debate import views


urlpatterns = [
    path('random-topic/', views.random_topic, name='random_topic'),
]
