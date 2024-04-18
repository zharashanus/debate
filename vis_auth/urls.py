from django.contrib import admin
from django.urls import path


# На это:
from my_auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register_user, name='register'),
    path('/register', views.register_page, name='register_page'),
    # path('api/login/', views.login_user, name='login'),  # Закомментировано
    # path('api/users/', views.get_all_users, name='get-users'),
]
