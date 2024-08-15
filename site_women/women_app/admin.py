from django.contrib import admin
from django.db.models.functions import Length
from .models import *


# Register your models here.

class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        if self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'bring_info')
    # для кликабельности
    list_display_links = ('title',)
    # чтобы менять значение в списке всех строк
    list_editable = ('is_published', 'cat')
    actions = ('set_published', 'set_draft')
    search_fields = ('title', 'cat__name')
    list_filter = (MarriedFilter, 'cat__name', 'is_published')
    exclude = ('is_published',)
    readonly_fields = ('slug',)
    filter_horizontal = ('tags',)

    # для пользовательского поля
    # сортировка в данном случае по кол-ву символов поля
    @admin.display(description='Краткое описание', ordering=Length('content'))
    def bring_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Отправить в черновик выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'Изменено {count} записей')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)
    exclude = ('slug',)

admin.site.site_header = 'Панель администрирования'
