from django.contrib import admin

from ServiceKGServer.models import Category, Advertisement


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['name', 'parent']


admin.site.register(Category, CategoryAdmin)


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id', 'position', 'phone', 'active']


admin.site.register(Advertisement, AdvertisementAdmin)
