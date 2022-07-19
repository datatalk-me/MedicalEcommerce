from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def product_images(self, obj):
         return format_html('<img src="{}" width="40"  />'.format(obj.product_image.url))

    list_display = ('product_images','product_name', 'product_slug', 'product_price','product_stock','product_available','product_updated_date')
    list_filter = ('product_name', 'product_slug','product_price', )
    search_fields = ('product_name', 'product_slug', 'product_price',)
    ordering = ('product_name', 'product_slug', 'product_price',)
    prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)