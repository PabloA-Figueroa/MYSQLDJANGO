from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from estados.models import Estado

 # Asegúrate de que estos campos existan en tu modelo Emprendimiento

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

