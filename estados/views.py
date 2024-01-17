from django.shortcuts import render
from estados.models import Estado
from estados.serializers import EstadoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EstadoSerializer

    def get_queryset(self):
        queryset = Estado.objects.filter(usuario=self.request.user)
        termino_busqueda_emprendimiento = self.request.query_params.get('emprendimiento', None)

        if termino_busqueda_emprendimiento is not None:
            queryset = queryset.filter(emprendimiento__nombre__icontains=termino_busqueda_emprendimiento)

        return queryset
