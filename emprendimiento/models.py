from django.db import models
from users.models import User

class Emprendimiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    usuario = models.ManyToManyField(User)  # Relaciona cada emprendimiento con un usuario
    tipoEmprendimiento = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre



# Create your models here. sadasd
