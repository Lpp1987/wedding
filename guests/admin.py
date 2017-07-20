from django.contrib import admin

from guests.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    pass
