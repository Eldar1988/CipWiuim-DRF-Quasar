from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile, Company


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'user', 'professional', 'public', 'register_date')
    list_filter = ('public', 'register_date')
    list_editable = ('public',)
    search_fields = ('name', 'professional')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" width="50"')

    get_image.short_description = 'Фото'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'admin_profile', 'slug', 'public', 'register_date')
    list_filter = ('public', 'register_date')
    list_editable = ('slug', 'public')
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.logo}" width="50"')

    get_image.short_description = 'Лого'
