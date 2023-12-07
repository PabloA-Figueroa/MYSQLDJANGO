from rest_framework.routers import DefaultRouter
from comentarios.api.views import PostModelViewSet

router_post= DefaultRouter()

router_post.register(prefix='post',basename= 'post', viewset=PostModelViewSet)
