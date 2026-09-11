from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available", "featured")
    list_filter = ("available", "featured", "category")
    list_editable = ("price", "available", "featured")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
