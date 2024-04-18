from django.apps import AppConfig


# Измените это:
class AuthConfig(AppConfig):
    name = 'auth'

# На это:
class MyAuthConfig(AppConfig):
    name = 'my_auth'
