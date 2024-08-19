from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'image',
        'created_at',
        'download_count',
        'views_count',
        'rating',
        'category'
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    prepopulated_fields = {'slug': ('name',)}