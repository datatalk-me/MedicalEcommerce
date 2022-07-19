from django.contrib import admin
from .models import Category
from django.utils.html import format_html

# Register your models here.

# categoty model
class CategoryAdmin(admin.ModelAdmin):
    def category_images(self, obj):
        return format_html('<img src="{}" width="40"  />'.format(obj.category_image.url))

    prepopulated_fields: dict = {'category_slug': ('category_name',)}
    list_display: list = ('category_images','category_name', 'category_slug')
    list_display_links: list = ('category_name',)
    search_fields: list = ('category_name',)


admin.site.register(Category, CategoryAdmin)