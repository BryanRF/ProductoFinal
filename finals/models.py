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
        (False, 'Inactivo'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_grupo = models.CharField(max_length=15)
    grupo_descripcion = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    activo = models.BooleanField()
    responsable_grupo = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.codigo_grupo} - {self.grupo_descripcion}'

    def estado_activo(self):
        if self.activo:
            return "Activo"
        else:
            return "Inactivo"

    def estado_bloqueado(self):
        if self.activo:
            return "Activo"
        else:
            return "Bloqueado"
        
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

class Inventario(models.Model):
    ESTADO_INVENTARIO_CHOICES = (
        ('PENDIENTE', 'PENDIENTE'),
        ('EN PROGRESO', 'EN PROGRESO'),
        ('CERRADO', 'CERRADO'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha_inventario = models.DateTimeField()
    nro_inventario = models.IntegerField()
    responsable = models.ForeignKey('Personal', on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    total_inventario = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=11, choices=ESTADO_INVENTARIO_CHOICES)
    creado_por = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    def __str__(self):
        return str(self.nro_inventario)

class Personal(models.Model):
    TIPO_DOCUMENTO_CHOICES = (
        ('DNI', 'DNI'),
        ('Pasaporte', 'Pasaporte'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_personal = models.CharField(max_length=100)
    direccion_personal = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)
    nro_documento = models.CharField(max_length=11)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_personal

    
class ItemsInventario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    nro_item = models.IntegerField()
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    stock_fisico = models.DecimalField(max_digits=12, decimal_places=2)
    devoluciones_pendientes = models.DecimalField(max_digits=12, decimal_places=2)
    total_unidades_stock = models.DecimalField(max_digits=12, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)
    total_item = models.DecimalField(max_digits=12, decimal_places=2)

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
