from django.contrib import admin
from .models import Category,Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)