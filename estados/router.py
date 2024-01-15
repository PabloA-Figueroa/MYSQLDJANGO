from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from estados.views import EstadoViewSet

router = DefaultRouter()
router.register(r'estado', EstadoViewSet, basename='estado')  # Asegúrate de agregar el 'basename'

estado_router = NestedSimpleRouter(router, r'estado', lookup='estado')
estado_router.register(r'estado', EstadoViewSet, basename='estado-contenidoEstado')
urlpatterns = router.urls + estado_router.urls
