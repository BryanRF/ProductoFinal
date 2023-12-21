from django import forms
from .models import *
from django.forms.models import inlineformset_factory
#----------------------Empresa-------------------
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nro_documento', 'razon_social', 'direccion']

        widgets = {
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
#----------------------Articulos-------------------
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['codigo_sku', 'precio_unitario', 'descripcion', 'unidad_medida','cantidad_unidad_medida', 'grupo', 'linea', 'sublinea', 'empresa', 'marca']
        widgets = {
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_unidad_medida': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'linea': forms.Select(attrs={'class': 'form-control'}),
            'sublinea': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }
#----------------------Grupo Proveedor-------------------
class GruposProveedorForm(forms.ModelForm):
    class Meta:
        model = GruposProveedor
        fields = ['codigo_grupo', 'grupo_descripcion', 'empresa', 'activo', 'responsable_grupo']

        widgets = {
            'codigo_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'activo': forms.Select(attrs={'class': 'form-select'},choices=((True, 'Activo'), (False, 'Bloqueado'))),
            'responsable_grupo': forms.TextInput(attrs={'class': 'form-control'}),
        }
#----------------------Marcas-------------------
class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = ['codigo_marca', 'marca_nombre']
        widgets = {
            'codigo_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
#----------------------Lineas Articulos-------------------
class LineasArticulosForm(forms.ModelForm):
    class Meta:
        model = LineasArticulos
        fields = ['codigo_linea', 'linea_descripcion', 'grupo', 'activo', 'responsable_linea']
    widgets = {
        'codigo_linea': forms.TextInput(attrs={'class': 'form-control'}),
        'linea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        'grupo': forms.Select(attrs={'class': 'form-control'}),
        'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'responsable_linea': forms.TextInput(attrs={'class': 'form-control'}),
    }
#----------------------Sucursal-------------------
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['empresa', 'nombre_comercial', 'direccion']

        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
#----------------------Sublineas-Articulos-------------------
class SublineasArticulosForm(forms.ModelForm):
    class Meta:
        model = SublineasArticulos
        fields = ['codigo_sublinea', 'sublinea_descripcion', 'linea', 'estado']

    # Agrega clases de Bootstrap a los widgets de los campos
    widgets = {
        'codigo_sublinea': forms.TextInput(attrs={'class': 'form-control'}),
        'sublinea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        'linea': forms.Select(attrs={'class': 'form-select'}),
        'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
#----------------------Unidades de Medida-------------------
class UnidadesMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadesMedida
        fields = ['unidad_nombre']
        widgets = {
            'unidad_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
#----------------------Usuarios-------------------
class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'full_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
#----------------------Canal Cliente-------------------
class CanalClienteForm(forms.ModelForm):
    class Meta:
        model = CanalCliente
        fields = ['canal_cliente_descripcion']

        widgets = {
            'canal_cliente_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
#----------------------Clientes-------------------
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nro_documento', 'nombre_razon_social', 'direccion', 'canal_cliente']

        widgets = {
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'canal_cliente': forms.Select(attrs={'class': 'form-control'}),
        }
#------------------Condicones Venta--------------
class CondicionVentasForm(forms.ModelForm):
    class Meta:
        model = CondicionVentas
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'genera_credito': forms.TextInput(attrs={'class': 'form-control'}),
        }

#----------------------TipoIdentificacion-------------------

class TiposIdentificacionForm(forms.ModelForm):
    class Meta:
        model = TiposIdentificacion
        fields = ['tipo_identificacion_nombre']
#----------------------TipoPedido-------------------

class TipoPedidoForm(forms.ModelForm):
    class Meta:
        model = TipoPedido
        fields = ['tipo_pedido_nombre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

#----------------------Vendedores-------------------
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_identificacion': forms.Select(attrs={'class': 'form-select'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'nro_movil': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
        }
#----------------------Notas Ventas-------------
class NotasVentaForm(forms.ModelForm):
    class Meta:
        model = NotasVenta
        fields = [
                   'empresa',
                   'sucursal',
                   'tipo_pedido',
                   'cliente',
                   'plazo',
                     'condicion_venta']
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'sucursal': forms.Select(attrs={'class': 'form-control'}),
            'tipo_pedido': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'condicion_venta': forms.Select(attrs={'class': 'form-control'}),
            'plazo': forms.NumberInput(attrs={'class': 'form-control'}),
        }


#----------------------ITEM Notas Ventas-------------

class ItemsNotaVentaForm(forms.ModelForm):
    class Meta:
        model = ItemsNotaVenta
        fields = [ 'articulo', 'cantidad']

        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

#----------------------PROMOCIONES-------------

from django import forms

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = [
            'tipo_promocion',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'tipo_cliente',
            'articulo_aplicable',
            'cantidad_minima_compra',
            'cantidad_maxima_compra',
            'unidades_bonificadas',
            'monto_maximo',
            'monto_minimo',
            'porcentaje_descuento',
            'proveedor',
            'articulo_bonificacion',
            'unidades_bonificadas',
        ]

        widgets = {
            'tipo_promocion': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-control'}),
            'articulo_aplicable': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_minima_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_maxima_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'porcentaje_descuento': forms.NumberInput(attrs={'class': 'form-control'}),  
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'articulo_bonificacion': forms.Select(attrs={'class': 'form-control'}),
            'unidades_bonificadas': forms.NumberInput(attrs={'class': 'form-control'}),
        }

