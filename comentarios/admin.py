from django.contrib import admin
from comentarios.models import comentarios

class comentariosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'contenido']


# Register your models here.
