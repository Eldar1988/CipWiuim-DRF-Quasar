from django.contrib import admin
from .models import MapPoint, Region, PointType


@admin.register(PointType)
class PointTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_region_points_count', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}

    def get_region_points_count(self, obj):
        points = MapPoint.objects.filter(region_id=obj.id).count()
        return points

    get_region_points_count.short_description = 'Кол-во объектов'


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_region_points_count', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}

    def get_region_points_count(self, obj):
        points = MapPoint.objects.filter(region_id=obj.id).count()
        return points

    get_region_points_count.short_description = 'Кол-во объектов'


@admin.register(MapPoint)
class MapPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'slug')
    list_filter = ('region', 'type', 'pub_date')
    search_fields = ('title', 'map_title')
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('type',)

