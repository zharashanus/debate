from django.contrib import admin
from django.urls import path, include


# На это:
from debate import views


urlpatterns = [
    path('random-topic/', views.random_topic, name='random_topic'),
    path("", include("my_auth.urls")),
    path("debate/", include("debate.urls")),
    # path('api/login/', views.login_user, name='login'),  # Закомментировано
    # path('api/users/', views.get_all_users, name='get-users'),
]
