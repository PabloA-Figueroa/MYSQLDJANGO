from xml.dom import ValidationErr
from django.contrib import admin
from Cursos.models import Cursos, ContenidoCurso,  Recurso, RecursoTexto, RecursoImagen, RecursoVideo
from django.db import models
from django import forms
from django.forms import Textarea
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline

class ContenidoCursoInline(admin.StackedInline):
    model = ContenidoCurso.cursos.through
    extra = 1
    verbose_name = "Agregar Contenido para el Curso"
    verbose_name_plural = "Agregar Contenido para el Curso"
    template = 'stacked.html'
    

# Define inlines for each resource type
class RecursoTextoInline(StackedPolymorphicInline.Child):
    model = RecursoTexto

class RecursoImagenInline(StackedPolymorphicInline.Child):
    model = RecursoImagen

class RecursoVideoInline(StackedPolymorphicInline.Child):
    model = RecursoVideo

# Base polymorphic inline for Recurso
class RecursoInline(StackedPolymorphicInline):
    model = Recurso
    child_inlines = (
        RecursoTextoInline,
        RecursoImagenInline,
        RecursoVideoInline,
    )

# Admin para ContenidoCurso
@admin.register(ContenidoCurso)
class ContenidoCursoAdmin(PolymorphicInlineSupportMixin,admin.ModelAdmin):
    inlines = [RecursoInline]
    list_display = ['titulo']
    search_fields = ['titulo']
@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    # def display_temas(self, obj):
    #    return ', '.join([tema.nombre for tema in obj.temas.all()])
   # display_temas.short_description = 'Temas'
    list_display = ['titulo', 'contenido']
    search_fields = ['titulo', 'contenido']
    list_filter = ('temas', 'fecha')
    inlines = [ContenidoCursoInline]
    fieldsets = (
        ('Información Básica', {'fields': ('titulo', 'imagen')}),
        ('Detalles del Curso', {'fields': ('contenido',  'temas')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


    #filter_horizontal = ['temas']






