from django import forms
from .models import *
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
        fields = ['codigo_sku', 'descripcion', 'unidad_medida', 'grupo', 'linea', 'sublinea', 'empresa', 'factor_compra', 'factor_reparto', 'marca']
        widgets = {
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'linea': forms.Select(attrs={'class': 'form-control'}),
            'sublinea': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'factor_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'factor_reparto': forms.NumberInput(attrs={'class': 'form-control'}),
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
            'activo': forms.Select(attrs={'class': 'form-select'},choices=((True, 'Activo'), (False, 'Inactivo'))),
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
        fields = '__all__'

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
        fields = ['id', 'unidad_nombre']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
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