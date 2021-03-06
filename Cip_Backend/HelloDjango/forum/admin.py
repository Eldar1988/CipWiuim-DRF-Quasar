from django.contrib import admin
from .models import Theme, Answer


class ThemeAnswersInline(admin.StackedInline):
    model = Answer
    exclude = ('email', 'profile')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'project', 'order', 'slug', 'views', 'pub_date')
    list_editable = ('author', 'order', 'slug')
    list_filter = ('author', 'project', 'pub_date', 'update')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ThemeAnswersInline]
    save_on_top = True
    save_as = True


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'public', 'pub_date')
    search_fields = ('name', 'text')
    list_filter = ('theme', 'pub_date')

    save_as = True
    save_on_top = True

