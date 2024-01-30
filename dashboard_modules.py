from jet.dashboard.modules import DashboardModule
from django.db.models import Sum
from estados.models import Estado  # Asegúrate de reemplazar esto con tu modelo real

class VentasDashboardModule(DashboardModule):
    title = 'Estado'
    template = 'tu_app/dashboard_modules/ventas_dashboard.html'

    def init_with_context(self, context):
        ventas_diarias = Estado.objects.aggregate(ventas_diarias=Sum('ingresoTotal'))
        ventas_mensuales = Estado.objects.aggregate(ventas_mensuales=Sum('gastoTotal'))
        ventas_anuales = Estado.objects.aggregate(ventas_anuales=Sum('beneficiosTotal'))

        self.children = [
            {'label': 'Ventas Diarias', 'valor': ventas_diarias['ventas_diarias']},
            {'label': 'Ventas Mensuales', 'valor': ventas_mensuales['ventas_mensuales']},
            {'label': 'Ventas Anuales', 'valor': ventas_anuales['ventas_anuales']}
        ]
