from django.contrib import admin
from .models import User, Customer

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'subject', 'message')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telephone', 'subject', 'message')

admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
