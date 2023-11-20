from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
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

def editar_unidad_medida(request, id):
    unidad = get_object_or_404(UnidadesMedida, id=id)
    if request.method == 'POST':
        form = UnidadesMedidaForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades_medida')
    else:
        form = UnidadesMedidaForm(instance=unidad)
    return render(request, 'unidad_medida/agregar_editar_unidad_medida.html', {'form': form})

def eliminar_unidad_medida(request, id):
    unidad = get_object_or_404(UnidadesMedida, id=id)
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