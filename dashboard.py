from django.utils.translation import gettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        # Listado de Enlaces
        self.children.append(modules.LinkList(
            _('Enlaces Útiles'),
            children=[
                {'title': _('Documentación de Django'), 'url': 'http://docs.djangoproject.com/', 'external': True},
                # Otros enlaces que consideres útiles
            ],
            column=0,
            order=0
        ))

        # Lista de Aplicaciones
        self.children.append(modules.AppList(
            _('Aplicaciones'),
            exclude=('auth.*',),
            column=1,
            order=0
        ))

        # Lista de Modelos
        self.children.append(modules.ModelList(
            _('Modelos'),
            exclude=('auth.*',),
            column=1,
            order=1
        ))

        # Acciones Recientes
        self.children.append(modules.RecentActions(
            _('Acciones Recientes'),
            5,
            column=2,
            order=0
        ))

        # Feed RSS (ejemplo con Django News)
        self.children.append(modules.Feed(
            _('Noticias de Django'),
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5,
            column=2,
            order=1
        ))


        # Aquí podrías añadir Google Analytics o Yandex Metrika Widgets si los tienes configurados
        # ...