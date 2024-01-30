"""
URL configuration for djangoProjectWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.template.defaulttags import url

from camaraComercio.views import inicioCurso  # Asegúrate de importar tu función de vista


from django.urls import path, re_path, include, reverse_lazy
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserLogIn, UserDetailAPIView
from django.conf.urls.static import static
from django.conf import settings

from estados.router import urlpatterns as estado_urlpatterns
from estados import views
from comentarios.api.router import router_post
from Cursos.router import urlpatterns as curso_urlpatterns
from emprendimiento.router import urlpatterns as emprendimiento_urlpatterns
from inventario.router import urlpatterns as inventario_urlpatterns
from Cursos.views import dashboard_view
router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inicioCurso/', inicioCurso, name='inicioCurso'),
    path('api-login/', UserLogIn.as_view(), name='api-login'),

    path('api-vista/', include(router_post.urls)),
    path('api-curso/', include(curso_urlpatterns)),
    path('api-estado/', include(estado_urlpatterns)),
    path('apid-edit-users/', UserDetailAPIView.as_view(), name='user-detail'),
    path('api-emp/', include(emprendimiento_urlpatterns)),
    path('api-inv/', include(inventario_urlpatterns)),
    path('estado/<int:pk>/', views.EstadoDetalleView.as_view(), name='detalle-estado'),
    path('api/', include(router.urls)),
    path('api-user-login/', UserLogIn.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
