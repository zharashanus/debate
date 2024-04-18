from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BasicUser

class BasicUserAdmin(UserAdmin):
    model = BasicUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(BasicUser, BasicUserAdmin)
