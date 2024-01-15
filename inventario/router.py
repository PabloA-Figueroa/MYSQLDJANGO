from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from inventario.views import InventarioViewSet

router = DefaultRouter()
router.register(r'inventario', InventarioViewSet, basename='inventario')  # Asegúrate de agregar el 'basename'

inventario_router = NestedSimpleRouter(router, r'inventario', lookup='inventario')
inventario_router.register(r'inventario', InventarioViewSet, basename='inventario-contenidoInventario')
urlpatterns = router.urls + inventario_router.urls