from djongo import models
from django.forms import JSONField
from emprendimiento.models import Emprendimiento
from users.models import User
from djongo import models as djongo_models

# Crear un modelos de estado que tenga 6 campos numericos

class Estado(models.Model):

    fecha = models.DateField()
    precioVentaPorUnidad = models.IntegerField(null=True, blank=True)
    cantidadProyectada = models.IntegerField(null=True, blank=True)
    ingresosAdicionales = models.IntegerField(null=True, blank=True)
    costoPorUnidad = models.IntegerField(null=True, blank=True)
    gastosOperativos = models.IntegerField(null=True, blank=True)
    gastosMarketing = models.IntegerField(null=True, blank=True)
    gastosDesarrollo = models.IntegerField(null=True, blank=True)
    gastosAdicionales = models.IntegerField(null=True, blank=True)
    ingresos = models.IntegerField(null=True, blank=True)
    gastos = models.IntegerField(null=True, blank=True)
    beneficios = models.IntegerField(null=True, blank=True)

    # Campos JSON para ingresos y gastos
    camposIngreso = JSONField( )
    camposGasto = JSONField( )
    # Nuevos campos
    usuario = models.ManyToManyField(User,  blank=True)
    emprendimiento = models.ManyToManyField(Emprendimiento, blank=True)
    tipoGasto = models.TextField(null=True, blank=True)
    valorGasto = models.IntegerField(null=True, blank=True)
    tipoIngreso = models.TextField(null=True, blank=True)
    valorIngreso = models.IntegerField(null=True, blank=True)
