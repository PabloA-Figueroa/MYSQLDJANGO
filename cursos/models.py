
# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from polymorphic.models import PolymorphicModel

class Tema(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='temas/', null=True, blank=True)
    def __str__(self):
        return self.nombre
    

class Cursos(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    temas = models.ManyToManyField(Tema, blank=True)
    def __str__(self):
        return self.titulo

class ContenidoCurso(models.Model):
    titulo = models.CharField(max_length=400)
    concepto = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='contenidos/', blank=True, null=True)
    cursos = models.ManyToManyField(Cursos,blank=True)
    def __str__(self):
        return self.titulo

class Recurso(PolymorphicModel):
    contenido_curso = models.ForeignKey(ContenidoCurso, on_delete=models.CASCADE)
    nombre  = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class RecursoTexto(Recurso):
    texto = RichTextField(blank=True, null=True)

class RecursoImagen(Recurso):
    imagen = models.ImageField(upload_to='recursos/imagenes/')

class RecursoVideo(Recurso):
    video = models.FileField(upload_to='recursos/videos/')
    url_video = models.URLField(blank=True, null=True)