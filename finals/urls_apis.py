# from rest_framework import routers
from django.urls import path
from .apis import ItemsNotaVentaAPIView
# router = routers.DefaultRouter()
# router.register(r'items-nota-venta', ItemsNotaVentaViewSet)

urlpatterns = [
    path('items-nota-venta/', ItemsNotaVentaAPIView.as_view(), name='items-nota-venta'),
]

# urlpatterns += router.urls
