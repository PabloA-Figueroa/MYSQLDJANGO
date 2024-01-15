from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from inventario.models import Inventario
from inventario.serializers import InventarioSerializer
# Create your views here.
class InventarioViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = InventarioSerializer

    def get_queryset(self):
        queryset = Inventario.objects.all()
        emprendimiento_id = self.request.query_params.get('emprendimiento', None)

        if emprendimiento_id is not None:
            # Filtra por ID de emprendimiento
            queryset = queryset.filter(emprendimiento__id=emprendimiento_id)
        return queryset