from django.db import models
from django.utils import timezone
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
    

#----------------------Articulo-------------------

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
        return f'{self.codigo_grupo} - {self.grupo_descripcion} '

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
        return f"{self.codigo_linea}  - {self.linea_descripcion} "

    
class SublineasArticulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_sublinea = models.CharField(max_length=15)
    sublinea_descripcion = models.CharField(max_length=100)
    linea = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.codigo_sublinea}  - {self.sublinea_descripcion} "
    

class UnidadesMedida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        return f"{self.nro_documento}  - {self.nombre_razon_social} "

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(default=timezone.now) #da la fecha automatico
    tipo_pedido = models.ForeignKey(TipoPedido, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    condicion_venta = models.ForeignKey(CondicionVentas, on_delete=models.CASCADE)
    plazo = models.IntegerField()
    total_pedido = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True) 
    nro_pedido = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.nro_pedido:
            ultimo_numero_pedido = NotasVenta.objects.filter(cliente=self.cliente).order_by('-fecha_pedido', '-id').values_list('nro_pedido', flat=True).first()
            self.nro_pedido = ultimo_numero_pedido + 1 if ultimo_numero_pedido else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.nro_pedido)
    #-----------ITEM NOtas Vendedor--------------

class ItemsNotaVenta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nota_venta = models.ForeignKey(NotasVenta, on_delete=models.CASCADE)
    nro_item = models.IntegerField(default=0)
    descripcion = models.JSONField(null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    total_item_bruto = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    factor_descuento = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    descuento_unitario = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    total_item = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    es_bonificacion = models.BooleanField(default=False)

    def calcular_factor_descuento(self):
        precio_unitario = self.articulo.precio_unitario
        total_sin_descuento = precio_unitario * self.cantidad
        total_con_descuento = total_sin_descuento - self.total_item
        self.factor_descuento =total_con_descuento
    def calcular_total_item(self):
        self.total_item_bruto = (self.articulo.precio_unitario) * self.cantidad
        descuento = (self.articulo.precio_unitario * self.descuento_unitario) / 100
        self.total_item = (self.articulo.precio_unitario - descuento) * self.cantidad

    def save(self, *args, **kwargs):
        self.calcular_total_item()
        self.calcular_factor_descuento()  # Calcula el factor de descuento antes de guardar
        if not self.nro_item and self.nota_venta:
            ultimo_item = ItemsNotaVenta.objects.filter(nota_venta=self.nota_venta).order_by('-nro_item').first()
            if ultimo_item:
                self.nro_item = ultimo_item.nro_item + 1
            else:
                self.nro_item = 1
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nro_item} - Total: {self.total_item}"
    

    #-----------PROMOCIONES-------------

class Promocion(models.Model):
    TIPO_PROMOCION_CHOICES = [
        ('caso_1', 'Descuento por Cantidad Comprada (1)'),
        ('caso_2', 'Bonificación por Monto Total (2)'),
        ('caso_3', 'Bonitifacion por productos y presentaciones(3)'),
        ('caso_4', 'Descuento por Rango de Cantidad (4)'),
        ('caso_5', 'Descuento por Rango de Monto (5)'),
        ('caso_7', 'Bonificación por escalas (7)'),
        ('caso_8', 'Bonificación por Cantidad Comprada gratis(8)'),
        ('caso_9', 'Bonificación y descuento por rango(9)'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_promocion = models.CharField(max_length=50, choices=TIPO_PROMOCION_CHOICES)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    tipo_cliente = models.ForeignKey(CanalCliente, on_delete=models.CASCADE, related_name='promociones', blank=True, null=True)
    cantidad_minima_compra = models.PositiveIntegerField(default=0, blank=True, null=True)#cantidad de productos comprados
    cantidad_maxima_compra = models.PositiveIntegerField(default=0, blank=True, null=True)
    monto_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2,default=0.0, blank=True, null=True) #cantidad x precio unitario
    porcentaje_descuento = models.DecimalField(max_digits=5,decimal_places=2, default=0.00,blank=True,null=True)
    proveedor = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE, related_name='promociones', blank=True, null=True)
    articulo_aplicable = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='productos_aplicables', blank=True, null=True)
    #solo si la promocion se aplica a un articulo
    articulo_bonificacion = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='productos_bonificacion', blank=True, null=True)
    unidades_bonificadas = models.PositiveIntegerField(default=0, blank=True, null=True)
    activo = models.BooleanField(default=False)

    def estado_activo(self):
        return "Activo" if self.activo else "Inactivo"
    def __str__(self):
        return self.descripcion


  #-----------uno a muchos articulos asociados-------------
class Promocion_articulos_asociados(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    cantidad_articulo = models.PositiveIntegerField(default=0, blank=True, null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

class Promocion_articulos_bonificados(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    cantidad_articulo = models.PositiveIntegerField(default=0, blank=True, null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)