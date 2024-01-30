from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class userAdmin(UserAdmin):
    fieldsets = (
        ('Información del Usuario', {'fields':('email', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name','bio', 'profile_pic')})
    )