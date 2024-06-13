from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.
class productAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.product_photo.url))

    thumbnail.short_description = 'Product Image'
    list_display = ('id','thumbnail','product_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'product_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'product_title', 'city', 'model', 'body_style','fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')
admin.site.register(Product,productAdmin)
