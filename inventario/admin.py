from django.contrib import admin
from inventario.models import Inventario
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['claseEmprendimiento', 'tipoProducto', 'cantidad', 'precio', 'comentario', 'mostrar_emprendimientos']
    search_fields = ['claseEmprendimiento', 'tipoProducto', 'cantidad', 'precio', 'comentario']

    def mostrar_emprendimientos(self, obj):
        return ", ".join([emprendimiento.nombre for emprendimiento in obj.emprendimiento.all()])
    mostrar_emprendimientos.short_description = 'Emprendimientos'
