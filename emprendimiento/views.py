from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from emprendimiento.models import Emprendimiento
from emprendimiento.serializers import EmprendimientoSerializer


# Create your views here.sadasd

class EmprendimientoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmprendimientoSerializer

    def get_queryset(self):

        queryset = Emprendimiento.objects.all()
        usuario_id = self.request.query_params.get('usuario', None)
        if usuario_id is not None:
            queryset = queryset.filter(usuario__id=usuario_id)
        return queryset
