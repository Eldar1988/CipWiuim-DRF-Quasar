from django.contrib import admin
from .models import Contact, Bot, SocialNetwork, CallBack

admin.site.register(Contact)
admin.site.register(Bot)
admin.site.register(SocialNetwork)


@admin.register(CallBack)
class CallBack(admin.ModelAdmin):
    list_display = ('name', 'phone', 'complete', 'date', 'update')
    list_editable = ('complete',)
    list_filter = ('complete', 'date', 'update')

