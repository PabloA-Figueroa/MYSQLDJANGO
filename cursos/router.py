from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from Cursos.views import CursoModelViewSet, ContenidoCursoViewSet

router = DefaultRouter()
router.register(r'curso', CursoModelViewSet)

curso_router = NestedSimpleRouter(router, r'curso', lookup='curso')
curso_router.register(r'contenidoCurso', ContenidoCursoViewSet, basename='curso-contenidoCurso')

urlpatterns = router.urls + curso_router.urls