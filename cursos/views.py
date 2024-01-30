from rest_framework.viewsets import ModelViewSet
from Cursos.models import Cursos, Tema, ContenidoCurso, Recurso
from Cursos.serializers import CursoSerializer,ContenidoCursoSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import render
from django.db.models import Sum, Count, Avg
from estados.models import Estado, Ingreso, Gasto
from users.models import User

class CursoModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CursoSerializer
    queryset = Cursos.objects.all()

class ContenidoCursoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContenidoCursoSerializer

    def get_queryset(self):
        return ContenidoCurso.objects.filter(cursos__id=self.kwargs['curso_pk'])


def dashboard_view(request):
    # Datos de los cursos
    cursos = Cursos.objects.all()
    total_cursos = cursos.count()

    # Datos financieros generales
    estados = Estado.objects.all()
    ingreso_total_general = estados.aggregate(Sum('ingresoTotal'))['ingresoTotal__sum'] or 0
    gasto_total_general = estados.aggregate(Sum('gastoTotal'))['gastoTotal__sum'] or 0
    beneficios_total_general = estados.aggregate(Sum('beneficiosTotal'))['beneficiosTotal__sum'] or 0

    # Datos de usuarios
    total_usuarios = User.objects.count()
    # Definir condiciones para usuarios activos, por ejemplo, usuarios con actividad reciente
    # usuarios_activos = User.objects.filter(condiciones).count()

    # Pasar datos al contexto
    context = {
        'total_cursos': total_cursos,
        'ingreso_total_general': ingreso_total_general,
        'gasto_total_general': gasto_total_general,
        'beneficios_total_general': beneficios_total_general,
        'total_usuarios': total_usuarios,
        # 'usuarios_activos': usuarios_activos,
        # Más datos según sea necesario
    }

    return render(request, 'dashboard_admin.html', context)