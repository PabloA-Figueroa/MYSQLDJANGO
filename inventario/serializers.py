from rest_framework.serializers import ModelSerializer
from inventario.models import Inventario
class InventarioSerializer(ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'