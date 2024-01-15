from rest_framework.serializers import ModelSerializer
from emprendimiento.models import Emprendimiento

class EmprendimientoSerializer(ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = '__all__'