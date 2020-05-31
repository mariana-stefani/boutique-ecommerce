from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Product)
admin.site.register(Category)