from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category, Comment, PostPhoto


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'category', 'rating', 'future', 'public', 'order', 'slug', 'views')
    list_editable = ('category', 'rating', 'future', 'public', 'order', 'slug')
    list_filter = ('category', 'future', 'public', 'pub_date', 'update')
    search_fields = ('title',)
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="50"')

    get_image.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    search_fields = ('title',)
    save_as = True
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'email', 'public', 'text', 'pub_date')
    list_editable = ('public',)
    list_filter = ('public', 'pub_date')
    search_fields = ('name', 'text')
    save_as = True
    save_on_top = True


@admin.register(PostPhoto)
class PostPhotoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'post', 'title', 'order', 'pub_date')
    list_editable = ('order',)
    list_filter = ('post', 'pub_date', 'update')
    search_fields = ('title',)
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" width="50"')

    get_image.short_description = 'Фото'
