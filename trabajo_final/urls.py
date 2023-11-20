from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path("empresa/", include("empresa.urls")),
    path("sucursal/", include("sucursal.urls")),
    path("inventario/", include("inventario.urls")),
    path("personal/", include("personal.urls")),
    path("grupo_proveedor/", include("grupo_proveedor.urls")),
    path("marcas/", include("marcas.urls")),
    path("unidad_medida/", include("unidad_medida.urls")),
    path("lineas/", include("lineas.urls")),
    path("sublineas/", include("sublineas.urls")),
    path("usuario/", include("usuario.urls")),
    path("articulos/", include("articulos.urls")),
    path("item_inventarios/", include("item_inventarios.urls")),
]
