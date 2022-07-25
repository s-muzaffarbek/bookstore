from django.contrib import admin
from .models import MyUser, Order


# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    search_fields = ('username',)

