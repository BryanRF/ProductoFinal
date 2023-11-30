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
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    sublinea = models.ForeignKey('SublineasArticulos', on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    factor_compra = models.IntegerField()
    factor_reparto = models.IntegerField()
    marca = models.ForeignKey('Marcas', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.codigo_sku}  - {self.descripcion} - s/. {self.precio_unitario}"

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
    def __str__(self):
        return self.descripcion

    #----------------------TipoIdentificacion-------------------
class TiposIdentificacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_identificacion_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_identificacion_nombre
    
    
#----------------------TIPOPedido-------------------

class TipoPedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_pedido_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_pedido_nombre
#----------------------Vendedores-------------------

class Vendedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendedor_codigo = models.CharField(max_length=15)
    tipo_identificacion = models.ForeignKey(TiposIdentificacion, on_delete=models.CASCADE)
    nro_documento = models.CharField(max_length=11)
    nombres = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    correo_electronico = models.CharField(max_length=255)
    nro_movil = models.CharField(max_length=15)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres
#-----------NOtas Vendedor--------------
class NotasVenta(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('Pasaporte', 'Pasaporte'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    nro_pedido = models.CharField(max_length=25)
    fecha_pedido = models.DateTimeField()
    tipo_pedido= models.ForeignKey(TipoPedido, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    condicion_venta = models.ForeignKey(CondicionVentas, on_delete=models.CASCADE)
    plazo= models.IntegerField()
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)
    total_pedido = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.nro_pedido
    
    #-----------ITEM NOtas Vendedor--------------

class ItemsNotaVenta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nota_venta = models.ForeignKey(NotasVenta, on_delete=models.CASCADE)
    nro_item = models.IntegerField(default=0)
    descripcion = models.JSONField(null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    total_item_bruto = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    factor_descuento = models.DecimalField(max_digits=12, decimal_places=3 , default=0)
    descuento_unitario = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    total_item = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    es_bonificacion = models.CharField(max_length=1 , default=0)
    def calcular_total_item(self):
        # Calcula el total_item automáticamente
        # total_item_bruto = 20  = 10*2
        self.total_item_bruto = (self.articulo.precio_unitario) * self.cantidad
        descuento = (self.articulo.precio_unitario * self.descuento_unitario) / 100
        self.total_item = (self.articulo.precio_unitario - descuento) * self.cantidad
    def save(self, *args, **kwargs):
        # Llama al método de cálculo al guardar el objeto
        self.calcular_total_item()
        # Si es un nuevo ítem y tiene una nota_venta asociada, incrementa el contador
        if not self.nro_item and self.nota_venta:
            ultimo_item = ItemsNotaVenta.objects.filter(nota_venta=self.nota_venta).order_by('-nro_item').first()
            if ultimo_item:
                self.nro_item = ultimo_item.nro_item + 1
            else:
                self.nro_item = 1
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nro_item} - Total: {self.total_item}"
