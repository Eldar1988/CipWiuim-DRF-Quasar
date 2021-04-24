from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project, DigitalIndicator, Benefit, Structure, QuestionAndAnswer, Review, ProjectVideo, \
    ProjectPhoto, ProjectFile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'company', 'project_admin', 'public', 'order', 'slug', 'views', 'pub_date')
    list_editable = ('public', 'order', 'slug')
    list_filter = ('company', 'public', 'pub_date', 'update')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="50"')

    get_image.short_description = 'Картинка'


@admin.register(DigitalIndicator)
class DigitalIndicatorAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order', 'value', 'max_value')
    list_filter = ('project', 'pub_date', 'update')
    list_editable = ('order', 'value', 'max_value', 'order')
    search_fields = ('title', 'value', 'max_value')
    save_on_top = True
    save_as = True


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order', 'icon')
    list_filter = ('project', 'pub_date', 'update')
    list_editable = ('project', 'icon', 'order')
    search_fields = ('title',)
    save_on_top = True
    save_as = True


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'project', 'order', 'slug', 'public', 'pub_date')
    list_editable = ('project', 'order', 'slug', 'public')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('project', 'public', 'pub_date', 'update')
    search_fields = ('title',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="50"')

    get_image.short_description = 'Картинка'


@admin.register(QuestionAndAnswer)
class QuestionAndAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'project', 'order', 'pub_date')
    list_editable = ('order', 'project')
    list_filter = ('project', 'pub_date', 'update')
    search_fields = ('title',)
    save_on_top = True
    save_as = True


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'project', 'order', 'public', 'pub_date')
    list_editable = ('project', 'order', 'public')
    list_filter = ('project', 'public', 'pub_date', 'update')
    search_fields = ('name',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar}" width="50"')
        return mark_safe(
            f'<img src="https://cdn.pixabay.com/photo/2017/04/15/04/36/incognito-2231825_960_720.png" width="50"')

    get_image.short_description = 'Аватар'


@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order', 'pub_date')
    list_filter = ('project', 'pub_date', 'update')
    list_editable = ('project', 'order')
    search_fields = ('title',)
    save_on_top = True
    save_as = True


@admin.register(ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'project', 'order', 'pub_date')
    list_filter = ('project', 'pub_date', 'update')
    list_editable = ('project', 'order')
    search_fields = ('title',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" width="50"')

    get_image.short_description = 'Картинка'


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order', 'pub_date')
    list_filter = ('project', 'pub_date', 'update')
    list_editable = ('project', 'order')
    search_fields = ('title',)
    save_on_top = True
    save_as = True


admin.site.site_title = 'CipWiuim'
admin.site.site_header = 'CipWiuim - администрирование'
