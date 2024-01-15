from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from emprendimiento.views import EmprendimientoViewSet

router = DefaultRouter()
router.register(r'emprendimiento', EmprendimientoViewSet, basename='emprendimiento')  # Asegúrate de agregar el 'basename'

emprendimiento_router = NestedSimpleRouter(router, r'emprendimiento', lookup='emprendimiento')
emprendimiento_router.register(r'emprendimiento', EmprendimientoViewSet, basename='emprendimiento-contenidoEmprendimiento')
urlpatterns = router.urls + emprendimiento_router.urls