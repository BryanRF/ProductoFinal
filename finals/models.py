from django.db import models

import uuid

class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nro_documento = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    def __str__(self):
        return self.razon_social
    
class Sucursal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre_comercial = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre_comercial 

class Articulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_sku = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150)
    unidad_medida = models.ForeignKey('UnidadesMedida', on_delete=models.CASCADE)
    grupo = models.ForeignKey('GruposProveedor', on_delete=models.CASCADE)
    linea = models.ForeignKey('LineasArticulos', on_delete=models.CASCADE)
    sublinea = models.ForeignKey('SublineasArticulos', on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    factor_compra = models.IntegerField()
    factor_reparto = models.IntegerField()
    marca = models.ForeignKey('Marcas', on_delete=models.CASCADE)
    def __str__(self):
        return self.codigo_sku

class GruposProveedor(models.Model):
    ESTADO_CHOICES = [
        (True, 'Activo'),
        (False, 'Bloqueado'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_grupo = models.CharField(max_length=15)
    grupo_descripcion = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    activo = models.BooleanField()
    responsable_grupo = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.codigo_grupo}'

    def estado_activo(self):
        if self.activo:
            return "Activo"
        else:
            return "Inactivo"
        
class LineasArticulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_linea = models.CharField(max_length=15)
    linea_descripcion = models.CharField(max_length=100)
    grupo = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE)
    activo = models.BooleanField()
    responsable_linea = models.CharField(max_length=25)
    def __str__(self):
        return self.codigo_linea

class SublineasArticulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_sublinea = models.CharField(max_length=15)
    sublinea_descripcion = models.CharField(max_length=100)
    linea = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE)
    estado = models.BooleanField()
    def __str__(self):
        return self.codigo_sublinea

class UnidadesMedida(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    unidad_nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.unidad_nombre

class Usuarios(models.Model):
    username = models.CharField(max_length=25)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)

    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username

class Marcas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_marca = models.CharField(max_length=14)
    marca_nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.marca_nombre

class CanalCliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    canal_cliente_descripcion = models.CharField(max_length=150)
    def __str__(self):
        return self.canal_cliente_descripcion
    
class Clientes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nro_documento = models.CharField(max_length=12)
    nombre_razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    canal_cliente = models.ForeignKey(CanalCliente,on_delete=models.CASCADE)
    def __str__(self):
        return self.nro_documento

class CondicionVentas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=100)
    genera_credito = models.CharField(max_length=10)