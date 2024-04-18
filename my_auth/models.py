from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class BasicUser(AbstractUser):
    role = models.CharField(
        max_length=255,
        choices=[('Линкольн', 'Линкольн'), ('Дуглас', 'Дуглас'), ('Lincoln', 'Lincoln'), ('Duoglas', 'Duoglas')],
        blank=True,
        null=True
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="basicuser_set",
        related_query_name="basicuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name="basicuser_set",
        related_query_name="basicuser",
    )
    class Meta:
           app_label = 'my_auth'