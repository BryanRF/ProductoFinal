from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST,require_http_methods
from .models import *
from .forms import *
from django.http import JsonResponse
#----------------------Empresa-------------------
def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/lista_empresas.html', {'empresas': empresas})

def agregar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()
    return render(request, 'empresa/agregar_editar_empresa.html', {'form': form})


def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm(instance=empresa)

    return render(request, 'empresa/agregar_editar_empresa.html', {'form': form})

def eliminar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    empresa.delete()
    return redirect('lista_empresas')
#----------------------Articulos-------------------
def listar_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulo/listar_articulos.html', {'articulos': articulos})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'articulo/crear_editar_articulo.html', {'form': form})

def editar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'articulo/crear_editar_articulo.html', {'form': form})

def eliminar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    articulo.delete()
    return redirect('listar_articulos')
#----------------------Grupo Proveedor-------------------
def listar_grupos_proveedor(request):
    grupos = GruposProveedor.objects.all()
    return render(request, 'grupo_proveedor/listar_grupos_proveedor.html', {'grupos': grupos})

def agregar_grupo_proveedor(request):
    if request.method == 'POST':
        form = GruposProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos_proveedor')
    else:
        form = GruposProveedorForm()
    return render(request, 'grupo_proveedor/agregar_editar_grupo_proveedor.html', {'form': form})

def editar_grupo_proveedor(request, grupo_proveedor_id):
    grupo = get_object_or_404(GruposProveedor, id=grupo_proveedor_id)
    if request.method == 'POST':
        form = GruposProveedorForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos_proveedor')
    else:
        form = GruposProveedorForm(instance=grupo)
    return render(request, 'grupo_proveedor/agregar_editar_grupo_proveedor.html', {'form': form, 'grupo': grupo})

def eliminar_grupo_proveedor(request, grupo_proveedor_id):
    grupo = get_object_or_404(GruposProveedor, id=grupo_proveedor_id)
    grupo.delete()
    return redirect('listar_grupos_proveedor')
#----------------------Marcas-------------------
def agregar_marca(request):
    if request.method == 'POST':
        form = MarcasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcasForm()
    return render(request, 'marca/agregar_editar_marca.html', {'form': form})

def listar_marcas(request):
    marcas = Marcas.objects.all()
    return render(request, 'marca/listar_marcas.html', {'marcas': marcas})

def editar_marca(request, marca_id):
    marca = get_object_or_404(Marcas, id=marca_id)
    if request.method == 'POST':
        form = MarcasForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcasForm(instance=marca)
    return render(request, 'marca/agregar_editar_marca.html', {'form': form})

def eliminar_marca(request, marca_id):
    marca = get_object_or_404(Marcas, id=marca_id)
    marca.delete()
    return redirect('listar_marcas')
#----------------------Lineas Articulos-------------------
# Listar LineasArticulos
def listar_lineas(request):
    lineas = LineasArticulos.objects.all()
    return render(request, 'lineas/listar_lineas.html', {'lineas': lineas})

# Crear LineasArticulos
def crear_linea(request):
    if request.method == 'POST':
        form = LineasArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_lineas')
    else:
        form = LineasArticulosForm()
    return render(request, 'lineas/crear_editar_linea.html', {'form': form})

# Editar LineasArticulos
def editar_linea(request, lineas_id):
    linea = get_object_or_404(LineasArticulos, id=lineas_id)
    if request.method == 'POST':
        form = LineasArticulosForm(request.POST, instance=linea)
        if form.is_valid():
            form.save()
            return redirect('listar_lineas')
    else:
        form = LineasArticulosForm(instance=linea)
    return render(request, 'lineas/crear_editar_linea.html', {'form': form})

# Eliminar LineasArticulos
def eliminar_linea(request, lineas_id):
    linea = get_object_or_404(LineasArticulos, id=lineas_id)
    linea.delete()
    return redirect('listar_lineas')
#----------------------Sucursales-------------------
def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/lista_sucursales.html', {'sucursales': sucursales})

def agregar_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sucursales')
    else:
        form = SucursalForm()
    return render(request, 'sucursal/agregar_editar_sucursal.html', {'form': form})

def editar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('lista_sucursales')
    else:
        form = SucursalForm(instance=sucursal)

    return render(request, 'sucursal/agregar_editar_sucursal.html', {'form': form})

def eliminar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    sucursal.delete()
    return redirect('lista_sucursales')
#----------------------Sublineas-Articulos-------------------
def listar_sublineas(request):
    sublineas = SublineasArticulos.objects.all()
    return render(request, 'sublineas/listar_sublineas.html', {'sublineas': sublineas})

def crear_sublinea(request):
    if request.method == 'POST':
        form = SublineasArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_sublineas')
    else:
        form = SublineasArticulosForm()
    return render(request, 'sublineas/crear_editar_sublinea.html', {'form': form})

def editar_sublinea(request, sublinea_id):
    sublinea = get_object_or_404(SublineasArticulos, id=sublinea_id)
    if request.method == 'POST':
        form = SublineasArticulosForm(request.POST, instance=sublinea)
        if form.is_valid():
            form.save()
            return redirect('listar_sublineas')
    else:
        form = SublineasArticulosForm(instance=sublinea)
    return render(request, 'sublineas/crear_editar_sublinea.html', {'form': form})

def eliminar_sublinea(request, sublinea_id):
    sublinea = get_object_or_404(SublineasArticulos, id=sublinea_id)
    sublinea.delete()
    return redirect('listar_sublineas')
#----------------------Unidades de Medida-------------------
def listar_unidades_medida(request):
    unidades = UnidadesMedida.objects.all()
    return render(request, 'unidad_medida/listar_unidades_medida.html', {'unidades': unidades})

def agregar_unidad_medida(request):
    if request.method == 'POST':
        form = UnidadesMedidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades_medida')
    else:
        form = UnidadesMedidaForm()
    return render(request, 'unidad_medida/agregar_editar_unidad_medida.html', {'form': form})

def editar_unidad_medida(request ,unidad_medida_id):
    unidad = get_object_or_404(UnidadesMedida, id=unidad_medida_id)
    if request.method == 'POST':
        form = UnidadesMedidaForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades_medida')
    else:
        form = UnidadesMedidaForm(instance=unidad)
    return render(request, 'unidad_medida/agregar_editar_unidad_medida.html', {'form': form})

def eliminar_unidad_medida(request, unidad_medida_id):
    unidad = get_object_or_404(UnidadesMedida, id=unidad_medida_id)
    unidad.delete()
    return redirect('listar_unidades_medida')
#----------------------Usuarios-------------------
def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuariosForm()
    return render(request, 'usuario/agregar_editar_usuario.html', {'form': form})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id=usuario_id)

    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuariosForm(instance=usuario)

    return render(request, 'usuario/agregar_editar_usuario.html', {'form': form})


def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    usuario.delete()
    return redirect('lista_usuarios')

#----------------------Canal Cliente-------------------
def lista_canales(request):
    canales = CanalCliente.objects.all()
    return render(request, 'canales/lista_canales.html', {'canales': canales})

def agregar_canal(request):
    if request.method == 'POST':
        form = CanalClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_canales')
    else:
        form = CanalClienteForm()
    return render(request, 'canales/agregar_editar_canal.html', {'form': form})

def editar_canal(request, canal_id):
    canal = get_object_or_404(CanalCliente, id=canal_id)

    if request.method == 'POST':
        form = CanalClienteForm(request.POST, instance=canal)
        if form.is_valid():
            form.save()
            return redirect('lista_canales')
    else:
        form = CanalClienteForm(instance=canal)

    return render(request, 'canales/agregar_editar_canal.html', {'form': form})

def eliminar_canal(request, canal_id):
    canal = get_object_or_404(CanalCliente, id=canal_id)
    canal.delete()
    return redirect('lista_canales')
#----------------------Clientes-------------------
def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClientesForm()
    return render(request, 'clientes/agregar_editar_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)

    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClientesForm(instance=cliente)

    return render(request, 'clientes/agregar_editar_cliente.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')
#------------------------Condiciones Venta-----------------
def lista_condicion_ventas(request):
    condicion_ventas = CondicionVentas.objects.all()
    return render(request, 'condicion_ventas/lista_condicion_ventas.html', {'condicion_ventas': condicion_ventas})

def agregar_condicion_venta(request):
    if request.method == 'POST':
        form = CondicionVentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_condicion_ventas')
    else:
        form = CondicionVentasForm()
    return render(request, 'condicion_ventas/agregar_editar_condicion_venta.html', {'form': form})

def editar_condicion_venta(request, condicion_venta_id):
    condicion_venta = get_object_or_404(CondicionVentas, id=condicion_venta_id)

    if request.method == 'POST':
        form = CondicionVentasForm(request.POST, instance=condicion_venta)
        if form.is_valid():
            form.save()
            return redirect('lista_condicion_ventas')
    else:
        form = CondicionVentasForm(instance=condicion_venta)

    return render(request, 'condicion_ventas/agregar_editar_condicion_venta.html', {'form': form})

def eliminar_condicion_venta(request, condicion_venta_id):
    condicion_venta = get_object_or_404(CondicionVentas, id=condicion_venta_id)
    condicion_venta.delete()
    return redirect('lista_condicion_ventas')


#----------------------TipoIdentificacion-------------------

def listar_tipos_identificacion(request):
    tipos_identificacion = TiposIdentificacion.objects.all()
    return render(request, 'tipos_identificacion/listar_tipos_identificacion.html', {'tipos_identificacion': tipos_identificacion})

def agregar_tipo_identificacion(request):
    if request.method == 'POST':
        form = TiposIdentificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_identificacion')
    else:
        form = TiposIdentificacionForm()

    return render(request, 'tipos_identificacion/agregar_editar_tipos_identificacion.html', {'form': form})

def editar_tipo_identificacion(request, tipo_identificacion_id):
    tipo_identificacion = get_object_or_404(TiposIdentificacion, id=tipo_identificacion_id)
    if request.method == 'POST':
        form = TiposIdentificacionForm(request.POST, instance=tipo_identificacion)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_identificacion')
    else:
        form = TiposIdentificacionForm(instance=tipo_identificacion)

    return render(request, 'tipos_identificacion/agregar_editar_tipos_identificacion.html', {'form': form})

def eliminar_tipo_identificacion(request, tipo_identificacion_id):
    tipo_identificacion = get_object_or_404(TiposIdentificacion, id=tipo_identificacion_id)
    tipo_identificacion.delete()
    return redirect('listar_tipos_identificacion')

#----------------------TipoPedido-------------------


# Lista de tipos de pedidos
def listar_tipos_pedido(request):
    tipos_pedido = TipoPedido.objects.all()
    return render(request, 'tipo_pedido/listar_tipos_pedido.html', {'tipo_pedido': tipos_pedido})

# Agregar un nuevo tipo de pedido
def agregar_tipo_pedido(request):
    if request.method == 'POST':
        form = TipoPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_pedido')
    else:
        form = TipoPedidoForm()
    return render(request, 'tipo_pedido/agregar_editar_tipo_pedido.html', {'form': form})

# Editar un tipo de pedido existente
def editar_tipo_pedido(request, tipo_pedido_id):
    tipo_pedido = get_object_or_404(TipoPedido, id=tipo_pedido_id)
    if request.method == 'POST':
        form = TipoPedidoForm(request.POST, instance=tipo_pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_pedido')
    else:
        form = TipoPedidoForm(instance=tipo_pedido)

    return render(request, 'tipo_pedido/agregar_editar_tipo_pedido.html', {'form': form, 'tipo_pedido': tipo_pedido})

# Eliminar un tipo de pedido existente
def eliminar_tipo_pedido(request, tipo_pedido_id):
    tipo_pedido = get_object_or_404(TipoPedido, id=tipo_pedido_id)
    tipo_pedido.delete()
    return redirect('listar_tipos_pedido')


#----------------------Vendedores-------------------

def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/listar_vendedores.html', {'vendedores': vendedores})

def agregar_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vendedores')
    else:
        form = VendedorForm()
    return render(request, 'vendedor/agregar_editar_vendedor.html', {'form': form})

def editar_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('listar_vendedores')
    else:
        form = VendedorForm(instance=vendedor)

    return render(request, 'vendedor/agregar_editar_vendedor.html', {'form': form})

def eliminar_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    vendedor.delete()
    return redirect('listar_vendedores')

#--------------------Notas Ventas-------------------
def lista_notas_venta(request):
    notas_venta = NotasVenta.objects.all()
    return render(request, 'notas_venta/lista_notas_venta.html', {'notas_venta': notas_venta})

def agregar_nota_venta(request):
    if request.method == 'POST':
        form = NotasVentaForm(request.POST)
        if form.is_valid():
            nota_venta = form.save()
            # Obtén todos los datos de la nota_venta
            nota_venta_data = {
                'id': nota_venta.id,
            }
            return redirect('agregar_item_nota_venta', **nota_venta_data)
    else:
        form = NotasVentaForm()
    
    return render(request, 'notas_venta/agregar_editar_nota_venta.html', {'form': form})

def editar_nota_venta(request, nota_venta_id):
    nota_venta = get_object_or_404(NotasVenta, id=nota_venta_id)
    if request.method == 'POST':
        form = NotasVentaForm(request.POST, instance=nota_venta)
        if form.is_valid():
            form.save()
            return redirect('lista_notas_venta')
    else:
        form = NotasVentaForm(instance=nota_venta)

    return render(request, 'notas_venta/agregar_editar_nota_venta.html', {'form': form})

def eliminar_nota_venta(request, nota_venta_id):
    nota_venta = get_object_or_404(NotasVenta, id=nota_venta_id)
    nota_venta.delete()
    return redirect('lista_notas_venta')


#-----------------------ITEM Notas Ventas--------------
def lista_items_nota_venta(request):
    items_nota_venta = ItemsNotaVenta.objects.all()
    return render(request, 'item_nota_venta/lista_items_nota_venta.html', {'items_nota_venta': items_nota_venta})

def agregar_item_nota_venta(request, id):
    nota_venta = NotasVenta.objects.get(id=id)
    if request.method == 'POST':
        form = ItemsNotaVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_items_nota_venta')
    else:
        form = ItemsNotaVentaForm()

    # Puedes acceder a los valores de id, tipo_pedido y cliente aquí
    nota_venta_data = {
        'id': nota_venta.id,
        'tipo_pedido': nota_venta.tipo_pedido.tipo_pedido_nombre,
        'cliente': nota_venta.cliente.nombre_razon_social,
        'tipo_cliente': nota_venta.cliente.canal_cliente.canal_cliente_descripcion,
    }

    return render(request, 'item_nota_venta/agregar_editar_item_nota_venta.html', {'form': form, 'nota_venta_data': nota_venta_data})

def editar_item_nota_venta(request, item_id):
    item_nota_venta = get_object_or_404(ItemsNotaVenta, id=item_id)
    if request.method == 'POST':
        form = ItemsNotaVentaForm(request.POST, instance=item_nota_venta)
        if form.is_valid():
            form.save()
            return redirect('lista_items_nota_venta')
    else:
        form = ItemsNotaVentaForm(instance=item_nota_venta)

    return render(request, 'item_nota_venta/agregar_editar_item_nota_venta.html', {'form': form})

def eliminar_item_nota_venta(request, item_id):
    item_nota_venta = get_object_or_404(ItemsNotaVenta, id=item_id)
    item_nota_venta.delete()
    return redirect('lista_items_nota_venta')



#-----------PROMOCIONES-------------

def lista_promociones(request):
    promociones = Promocion.objects.all()
    return render(request, 'promocion/lista_promociones.html', {'promociones': promociones})

# Vista para agregar una nueva promoción
def agregar_promocion(request):
    articulos = Articulo.objects.all()
    if request.method == 'POST':
        form = PromocionForm(request.POST)
    else:
        form = PromocionForm()
    return render(
        request,
        'promocion/agregar_editar_promocion.html',
        {'form': form, 'articulos': articulos}
    )
# Vista para editar una promoción existente
def editar_promocion(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('lista_promociones')
    else:
        form = PromocionForm(instance=promocion)

    return render(request, 'promocion/agregar_editar_promocion.html', {'form': form})

# Vista para eliminar una promoción
def eliminar_promocion(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    promocion.delete()
    return redirect('lista_promociones')




