from django.shortcuts import render
from estado.models import Estado
from estado.serializers import EstadoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EstadoSerializer

    def get_queryset(self):
        queryset = Estado.objects.filter(usuario=self.request.user)
            # obtener el termino de busqueda desde la solicitud
        termino_busqueda_emprendimiento = self.request.query_params.get('emprendimiento', None)

        # si el termino de busqueda no es nulo, filtra el queryset por el termino de busqueda
        if termino_busqueda_emprendimiento is not None:
            queryset = queryset.filter(emprendimiento__nombre__icontains=termino_busqueda_emprendimiento)

        return queryset
