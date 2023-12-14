# from rest_framework import routers
from django.urls import path
from .apis import *
# router = routers.DefaultRouter()
# router.register(r'items-nota-venta', ItemsNotaVentaViewSet)

urlpatterns = [
    path('items-nota-venta/', ItemsNotaVentaAPIView.as_view(), name='items-nota-venta'),
    path('api/promociones/', promocion_list_create, name='promocion-list-create'),
]

# urlpatterns += router.urls
