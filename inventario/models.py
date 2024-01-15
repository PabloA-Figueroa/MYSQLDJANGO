from django.db import models
from emprendimiento.models import Emprendimiento

class Inventario(models.Model):
    emprendimiento = models.ManyToManyField(Emprendimiento, blank=True)
    claseEmprendimiento = models.CharField(max_length=60, null=True, blank=True)
    tipoProducto = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)
# Create your models here.
