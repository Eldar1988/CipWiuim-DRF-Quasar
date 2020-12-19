from django.contrib import admin
from .models import MapPoint, Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    search_fields = ('title',)
    save_as = True
    save_on_top = True


@admin.register(MapPoint)
class MapPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'x', 'y', 'map_title', 'slug')
    list_editable = ('region', 'x', 'y', 'map_title', 'slug')
    list_filter = ('region', 'pub_date')
    search_fields = ('title', 'map_title')
    save_as = True
    save_on_top = True
