# from rest_framework import routers
from django.urls import path
from .apis import *
# router = routers.DefaultRouter()
# router.register(r'items-nota-venta', ItemsNotaVentaViewSet)

urlpatterns = [
    path('items-nota-venta/', ItemsNotaVentaAPIView.as_view(), name='items-nota-venta'),
    path('api/promociones/', promocion_list_create, name='promocion-list-create'),
    path('obtener_items_nota_venta/<uuid:nota_venta_id>/', obtener_items_nota_venta, name='obtener_items_nota_venta'),
    path('api/eliminar_item_nota_venta/<uuid:item_id>/', eliminar_item_nota_venta_api, name='eliminar_item_nota_venta_api'),
    path('confirmar-nota-venta/<uuid:nota_venta_id>/', confirmar_nota_venta, name='confirmar_nota_venta'),
    path('promocion-update/<uuid:pk>/', ActivarInactivarPromocion.as_view(), name='activar_inactivar_promocion'),
]

# urlpatterns += router.urls
