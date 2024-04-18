from django.contrib import admin
from django.urls import path


# На это:
from my_auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register_user, name='register'),
    path('register/', views.register_page, name='register_page'),
    path('', views.main_page, name='main_page'), 
    path('login/', views.login_page, name='login_page'),
    path('random-topic/', views.random_topic, name='random_topic'),
    # path('api/login/', views.login_user, name='login'),  # Закомментировано
    # path('api/users/', views.get_all_users, name='get-users'),
]
