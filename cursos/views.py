from rest_framework.viewsets import ModelViewSet
from Cursos.models import Cursos, Tema, ContenidoCurso, Recurso
from Cursos.serializers import CursoSerializer,ContenidoCursoSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CursoModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CursoSerializer
    queryset = Cursos.objects.all()

class ContenidoCursoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContenidoCursoSerializer

    def get_queryset(self):
        return ContenidoCurso.objects.filter(cursos__id=self.kwargs['curso_pk']).prefetch_related('recurso_set')