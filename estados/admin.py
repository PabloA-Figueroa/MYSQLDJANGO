from django.contrib import admin
from estados.models import Estado
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['fecha']
    search_fields = ['fecha']

