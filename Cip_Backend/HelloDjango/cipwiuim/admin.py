from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CIPAbout, CIPReview, CIPPartner, CIPPartnerForm, PartnerFile, ForPartnerNotification, \
    NotificationFile, Rule, CIPPhoto, CIPVideo, CIPQuestionAnswer

admin.site.register(CIPAbout)
admin.site.register(CIPReview)
admin.site.register(CIPPartner)
admin.site.register(Rule)
admin.site.register(CIPVideo)
admin.site.register(CIPQuestionAnswer)


class PartnerFileInline(admin.TabularInline):
    model = PartnerFile


class PartnerNotificationInline(admin.TabularInline):
    model = ForPartnerNotification
    exclude = ('user',)


@admin.register(CIPPartnerForm)
class CIPPartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    search_fields = ('title',)
    save_on_top = True
    save_as = True
    inlines = [PartnerFileInline, PartnerNotificationInline]


@admin.register(PartnerFile)
class PartnerFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner_form')
    list_editable = ('partner_form',)
    search_fields = ('title',)
    list_filter = ('partner_form',)
    save_on_top = True
    save_as = True


class NotificationFilesInline(admin.TabularInline):
    model = NotificationFile


@admin.register(ForPartnerNotification)
class ForPartnerNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner_form', 'user', 'pub_date')
    list_editable = ('partner_form', 'user')
    search_fields = ('title',)
    list_filter = ('partner_form', 'pub_date', 'user')
    save_on_top = True
    save_as = True
    inlines = [NotificationFilesInline]


@admin.register(NotificationFile)
class NotificationFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'notification')
    list_editable = ('notification',)
    search_fields = ('title',)
    list_filter = ('notification',)
    save_on_top = True
    save_as = True


@admin.register(CIPPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order')
    list_editable = ('order',)
    list_filter = ('pub_date', 'update')
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" width="50"')

    get_image.short_description = 'Фото'