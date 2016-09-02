from django.contrib import admin

# Register your models here.
from ServiceKGServer.models import Category, Advertisement


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', ]
    list_filter = ['name', 'parent']


admin.site.register(Category, CategoryAdmin)


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id', 'position', 'phone']


admin.site.register(Advertisement, AdvertisementAdmin)
