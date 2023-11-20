from django.urls import path
from .views import *

urlpatterns = [
#----------------------Empresa-------------------
    path('lista_empresas/', lista_empresas, name='lista_empresas'),
    path('agregar_empresa/', agregar_empresa, name='agregar_empresa'),
    path('editar_empresa/<uuid:empresa_id>/', editar_empresa, name='editar_empresa'),
    path('eliminar_empresa/<uuid:empresa_id>/', eliminar_empresa, name='eliminar_empresa'),
#----------------------Articulos-------------------
    path('listar_articulos/', listar_articulos, name='listar_articulos'),
    path('crear_articulo/', crear_articulo, name='crear_articulo'),
    path('editar_articulo/<uuid:articulo_id>/', editar_articulo, name='editar_articulo'),
    path('eliminar_articulo/<uuid:articulo_id>/', eliminar_articulo, name='eliminar_articulo'),
#----------------------Grupo Proveedor-------------------
    path('listar_grupos_proveedor/', listar_grupos_proveedor, name='listar_grupos_proveedor'),
    path('agregar_grupo_proveedor/', agregar_grupo_proveedor, name='agregar_grupo_proveedor'),
    path('editar_grupo_proveedor/<uuid:grupo_proveedor_id>/', editar_grupo_proveedor, name='editar_grupo_proveedor'),
    path('eliminar_grupo_proveedor/<uuid:grupo_proveedor_id>/', eliminar_grupo_proveedor, name='eliminar_grupo_proveedor'),
#----------------------Marcas-------------------
    path('agregar_marca/', agregar_marca, name='agregar_marca'),
    path('listar_marcas/', listar_marcas, name='listar_marcas'),
    path('editar_marca/<uuid:marca_id>/', editar_marca, name='editar_marca'),
    path('eliminar_marca/<uuid:marca_id>/', eliminar_marca, name='eliminar_marca'),
#----------------------Lineas Articulos-------------------
    path('lineas/', listar_lineas, name='listar_lineas'),
    path('lineas/crear/', crear_linea, name='crear_linea'),
    path('lineas/editar/<uuid:lineas_id>/', editar_linea, name='editar_linea'),
    path('lineas/eliminar/<uuid:lineas_id>/', eliminar_linea, name='eliminar_linea'),
#----------------------Sucursales-------------------
    path('lista_sucursales/', lista_sucursales, name='lista_sucursales'),
    path('agregar_sucursal/', agregar_sucursal, name='agregar_sucursal'),
    path('editar_sucursal/<uuid:sucursal_id>/', editar_sucursal, name='editar_sucursal'),
    path('eliminar_sucursal/<uuid:sucursal_id>/', eliminar_sucursal, name='eliminar_sucursal'),
#----------------------Sublineas-Articulos-------------------
    path('sublineas/', listar_sublineas, name='listar_sublineas'),
    path('sublineas/crear/', crear_sublinea, name='crear_sublinea'),
    path('sublineas/editar/<uuid:sublinea_id>/', editar_sublinea, name='editar_sublinea'),
    path('sublineas/eliminar/<uuid:sublinea_id>/', eliminar_sublinea, name='eliminar_sublinea'),
#----------------------Unidades de Medida-------------------
    path('listar_unidades_medida/', listar_unidades_medida, name='listar_unidades_medida'),
    path('agregar_unidad_medida/', agregar_unidad_medida, name='agregar_unidad_medida'),
    path('editar_unidad_medida/<int:id>/', editar_unidad_medida, name='editar_unidad_medida'),
    path('eliminar_unidad_medida/<int:id>/', eliminar_unidad_medida, name='eliminar_unidad_medida'),
#----------------------Usuarios-------------------
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('agregar_usuario/', agregar_usuario, name='agregar_usuario'),
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
]
