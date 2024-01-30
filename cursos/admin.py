from xml.dom import ValidationErr
from django.contrib import admin
from Cursos.models import Cursos, ContenidoCurso, Recurso, RecursoTexto, RecursoImagen, RecursoVideo
from django.db import models
from django import forms
from django.forms import Textarea
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline
from django.utils.html import format_html
from jet.admin import CompactInline
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedPolymorphicInlineSupportMixin, NestedStackedPolymorphicInline


# Define inlines for each resource type
class RecursoTextoInline(NestedStackedPolymorphicInline.Child, NestedStackedInline):
    model = RecursoTexto

class RecursoImagenInline(NestedStackedPolymorphicInline.Child, NestedStackedInline):
    model = RecursoImagen

class RecursoVideoInline(NestedStackedPolymorphicInline.Child, NestedStackedInline):
    model = RecursoVideo

class RecursoInline(NestedStackedPolymorphicInline):
    model = Recurso
    child_inlines = (
        RecursoTextoInline,
        RecursoImagenInline,
        RecursoVideoInline,
    )
class ContenidoCursoInline(NestedStackedInline):
    model = ContenidoCurso
    extra = 1
    inlines = [RecursoInline]
    verbose_name = "Agregar Contenido para el Curso"
    verbose_name_plural = "Agregar Contenido para el Curso"


class RecursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contenido_curso', 'tipo_recurso']
    search_fields = ['nombre', 'contenido_curso__titulo']

    def tipo_recurso(self, obj):
        if isinstance(obj, RecursoTexto):
            return format_html('<span style="color: #ff0000;">Texto</span>')
        elif isinstance(obj, RecursoImagen):
            return format_html('<span style="color: #0000ff;">Imagen</span>')
        elif isinstance(obj, RecursoVideo):
            return format_html('<span style="color: #00ff00;">Video</span>')
        else:
            return 'Desconocido'

# Admin para ContenidoCurso
class ContenidoCursoAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [RecursoInline]
    list_display = ['titulo']
    search_fields = ['titulo']

@admin.register(Cursos)
class CursoAdmin(NestedPolymorphicInlineSupportMixin, NestedModelAdmin):
    list_display = ['titulo']
    search_fields = ['titulo', 'contenido']
    list_filter = ('fecha','titulo')
    inlines = [ContenidoCursoInline]
    fieldsets = (
        ('Información Básica', {'fields': ('titulo', 'imagen')}),
        ('Detalles del Curso', {'fields': ('contenido', )}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


    # filter_horizontal = ['temas']