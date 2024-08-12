from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    #для кликабельности
    list_display_links = ('id', 'title')
    #чтобы менять значение в списке всех строк
    list_editable = ('is_published', 'cat')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)


admin.site.site_header = 'Панель администрирования'