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
    path('editar_unidad_medida/<uuid:unidad_medida_id>/', editar_unidad_medida, name='editar_unidad_medida'),
    path('eliminar_unidad_medida/<uuid:unidad_medida_id>/', eliminar_unidad_medida, name='eliminar_unidad_medida'),
#----------------------Usuarios-------------------
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('agregar_usuario/', agregar_usuario, name='agregar_usuario'),
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
#----------------------Canal Cliente-------------------
    path('lista_canales/', lista_canales, name='lista_canales'),
    path('agregar_canal/', agregar_canal, name='agregar_canal'),
    path('editar_canal/<uuid:canal_id>/', editar_canal, name='editar_canal'),
    path('eliminar_canal/<uuid:canal_id>/', eliminar_canal, name='eliminar_canal'),
#----------------------Clientes-------------------
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('editar_cliente/<uuid:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<uuid:cliente_id>/', eliminar_cliente, name='eliminar_cliente'),
#-----------------Condiciones venta----------------
    path('lista_condicion_ventas/', lista_condicion_ventas, name='lista_condicion_ventas'),
    path('agregar_condicion_venta/', agregar_condicion_venta, name='agregar_condicion_venta'),
    path('editar_condicion_venta/<uuid:condicion_venta_id>/', editar_condicion_venta, name='editar_condicion_venta'),
    path('eliminar_condicion_venta/<uuid:condicion_venta_id>/', eliminar_condicion_venta, name='eliminar_condicion_venta'),

#----------------------TipoIdentificacion-------------------

    path('listar_tipos_identificacion/', listar_tipos_identificacion, name='listar_tipos_identificacion'),
    path('agregar_tipo_identificacion/', agregar_tipo_identificacion, name='agregar_tipo_identificacion'),
    path('editar_tipo_identificacion/<uuid:tipo_identificacion_id>/', editar_tipo_identificacion, name='editar_tipo_identificacion'),
    path('eliminar_tipo_identificacion/<uuid:tipo_identificacion_id>/', eliminar_tipo_identificacion, name='eliminar_tipo_identificacion'),

#----------------------TipoPedido-------------------
    path('listar_tipos_pedido/', listar_tipos_pedido, name='listar_tipos_pedido'),
    path('agregar_tipo_pedido/', agregar_tipo_pedido, name='agregar_tipo_pedido'),
    path('editar_tipo_pedido/<uuid:tipo_pedido_id>/', editar_tipo_pedido, name='editar_tipo_pedido'),
    path('eliminar_tipo_pedido/<uuid:tipo_pedido_id>/', eliminar_tipo_pedido, name='eliminar_tipo_pedido'),

#----------------------Vendedores-------------------
    path('listar_vendedores/', listar_vendedores, name='listar_vendedores'),
    path('agregar_vendedor/', agregar_vendedor, name='agregar_vendedor'),
    path('editar_vendedor/<uuid:vendedor_id>/', editar_vendedor, name='editar_vendedor'),
    path('eliminar_vendedor/<uuid:vendedor_id>/', eliminar_vendedor, name='eliminar_vendedor'),

#-----------------------Notas Ventas--------------
    path('lista_notas_venta/', lista_notas_venta, name='lista_notas_venta'),
    path('agregar_nota_venta/', agregar_nota_venta, name='agregar_nota_venta'),
    path('editar_nota_venta/<uuid:nota_venta_id>/', editar_nota_venta, name='editar_nota_venta'),
    path('eliminar_nota_venta/<uuid:nota_venta_id>/', eliminar_nota_venta, name='eliminar_nota_venta'),


#-----------------------ITEM Notas Ventas--------------

path('lista_items_nota_venta/', lista_items_nota_venta, name='lista_items_nota_venta'),
    # path('agregar_item_nota_venta/', agregar_item_nota_venta, name='agregar_item_nota_venta'),

    path('agregar_item_nota_venta/<uuid:id>/', agregar_item_nota_venta, name='agregar_item_nota_venta'),

    path('editar_item_nota_venta/<uuid:item_id>/', editar_item_nota_venta, name='editar_item_nota_venta'),
    path('eliminar_item_nota_venta/<uuid:item_id>/', eliminar_item_nota_venta, name='eliminar_item_nota_venta'),



    # ---------------------- Promociones -------------------
    path('lista_promociones/', lista_promociones, name='lista_promociones'),
    path('agregar_promocion/', agregar_promocion, name='agregar_promocion'),
    path('editar_promocion/<uuid:promocion_id>/', editar_promocion, name='editar_promocion'),
    path('eliminar_promocion/<uuid:promocion_id>/', eliminar_promocion, name='eliminar_promocion'),
    
    
]