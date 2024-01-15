
from emprendimiento.models import Emprendimiento
from django.contrib import admin


@admin.register(Emprendimiento)
class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
from django.contrib import admin

# Agregar mas modelos
