from djongo import models
from django.forms import JSONField
from emprendimiento.models import Emprendimiento
from users.models import User

class Estado(models.Model):
    fecha = models.DateField()
    beneficios = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Asumiendo que es un valor calculado
    usuario = models.ManyToManyField(User, blank=True)
    emprendimiento = models.ManyToManyField(Emprendimiento, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    ingresoTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gastoTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beneficiosTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
class Ingreso(models.Model):
    estado = models.ForeignKey(Estado, related_name='ingresos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Gasto(models.Model):
    estado = models.ForeignKey(Estado, related_name='gastos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)