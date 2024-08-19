from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'is_staff',
        'avatar',
        'status'
    ]

    filter_horizontal = [
        'download_games',
        'friends_online',
        'live_streams',
        'clips'
    ]