from django.contrib import admin
from .models import CustomUser,CustomerAddress
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display= ('username','email','first_name','last_name')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(CustomerAddress)