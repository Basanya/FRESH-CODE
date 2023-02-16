from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title", "category"]
    searh_fields = ["description", "category"]
    ordering = ["title", "-category", "description"]
    prepopulated_fields = {"slug" : ["title"]}

admin.site.register(Product,ProductAdmin)
    