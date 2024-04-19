from django.contrib import admin
from django.urls import path, include


# На это:
from my_auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register_user, name='register'),
    path('register/', views.register_page, name='register_page'),
    path('', views.main_page, name='main_page'), 
    path('login/', views.login_page, name='login_page'),
]
