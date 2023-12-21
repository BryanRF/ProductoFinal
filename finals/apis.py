from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST
@csrf_exempt
def promocion_list_create(request): #api para crear las promociones
    try:
         # Verifica si la solicitud es de tipo POST
        if request.method == 'POST':
            data = json.loads(request.body)
            # Convierte los datos del cuerpo de la solicitud JSON a un diccionario
            tipo_promocion = data.get('tipo_promocion')
            descripcion = data.get('descripcion')
            fecha_inicio = data.get('fecha_inicio')
            fecha_fin = data.get('fecha_fin')
            tipo_cliente_id = data.get('tipo_cliente')
            cantidad_minima_compra = data.get('cantidad_minima_compra')
            cantidad_maxima_compra = data.get('cantidad_maxima_compra')
            unidades_bonificadas = data.get('unidades_bonificadas')
            monto_minimo = data.get('monto_minimo')
            monto_maximo = data.get('monto_maximo')
            porcentaje_descuento = data.get('porcentaje_descuento')
            proveedor_id = data.get('proveedor')
            articulo_aplicable_id = data.get('articulo_aplicable')
            articulo_bonificacion_id = data.get('articulo_bonificacion')
            # Crea una nueva instancia
            promocion = Promocion.objects.create(
                tipo_promocion=tipo_promocion,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                tipo_cliente_id=tipo_cliente_id,
                cantidad_minima_compra=cantidad_minima_compra,
                cantidad_maxima_compra=cantidad_maxima_compra,
                unidades_bonificadas=unidades_bonificadas,
                monto_minimo=monto_minimo,
                monto_maximo=monto_maximo,
                porcentaje_descuento=porcentaje_descuento,
                proveedor_id=proveedor_id,
                articulo_aplicable_id=articulo_aplicable_id,
                articulo_bonificacion_id=articulo_bonificacion_id,
                activo=True,
            )

            # Procesa los datos de los artículos asociados
            articulos_asociados = data.get('articulosSeleccionadosModal', [])
            for articulo in articulos_asociados:
                cantidad = articulo.get('cantidad')
                articulo_id = articulo.get('id')
                Promocion_articulos_asociados.objects.create(
                    promocion=promocion,
                    cantidad_articulo=cantidad,
                    articulo_id=articulo_id
                )

            # Procesar los datos de los artículos bonificados
            articulos_bonificados = data.get('articulosSeleccionadosBonificadosModal', [])
            for articulo in articulos_bonificados:
                cantidad = articulo.get('cantidad')
                articulo_id = articulo.get('id')
                Promocion_articulos_bonificados.objects.create(
                    promocion=promocion,
                    cantidad_articulo=cantidad,
                    articulo_id=articulo_id
                )

            # Devuelve una respuesta JSON indicando que la promoción se creó con éxito
            return JsonResponse({'message': 'Promoción creada exitosamente', 'ok':True}, status=201)
    except Exception as e:
            # Captura excepciones generales y devuelve un mensaje de error
            return JsonResponse({'message': f'Error al procesar la solicitud: {str(e)}', 'ok':False}, status=500)

    return JsonResponse({'message': 'Método no permitido', 'ok':False}, status=405)



# Definición de una clase de vista basada en API para manejar los ítems de nota de venta
class ItemsNotaVentaAPIView(APIView):
    # Constructor de la clase
    def __init__(self, *args, **kwargs):
        super(ItemsNotaVentaAPIView, self).__init__(*args, **kwargs)
        self.messages = []  # Lista para almacenar mensajes relacionados con la venta
        self.nota_venta = None  # Variable para almacenar la instancia de NotasVenta
        self.serializer = None  # Variable para almacenar el serializer
        self.total_temporal = 0
        self.id_articulo = None
        self.cantidad_comprada = None
        self.item_nota_venta = None  # Variable global para almacenar el item de nota de venta

    # Método POST para procesar la creación de ítems de nota de venta
    def post(self, request, *args, **kwargs):
        self.serializer = ItemsNotaVentaSerializer(data=request.data)
        if self.serializer.is_valid():
            self.id_articulo = request.data.get('articulo')
            self.cantidad_comprada = self.serializer.validated_data['cantidad']
            self.nota_venta = NotasVenta.objects.get(pk=request.data.get('nota_venta'))
            self.item_nota_venta = ItemsNotaVenta.objects.filter(nota_venta=self.nota_venta, articulo_id=self.id_articulo).first()

            if self.item_nota_venta:
                self.item_nota_venta.cantidad = self.cantidad_comprada
                self.item_nota_venta.save()
            else:
                self.serializer.save()
                self.item_nota_venta = self.serializer.instance

            items_nota_venta = ItemsNotaVenta.objects.filter(nota_venta=self.nota_venta)
            self.total_temporal = sum(item.total_item for item in items_nota_venta)
            if self.item_nota_venta:
                ItemsNotaVenta.objects.filter(referencia_bonificacion=self.item_nota_venta).delete()
            self.caso1()
            self.caso2()
            self.caso3()
            self.caso4()
            self.caso5()
            self.caso7()
            self.caso8()
            self.caso9()

            data = {'message': self.get_messages()}
            # Calcula el total después del cálculo de todas las bonificaciones
            items_nota_venta_despues_bonificaciones = ItemsNotaVenta.objects.filter(nota_venta=self.nota_venta)
            total_despues_bonificaciones = sum(item.total_item for item in items_nota_venta_despues_bonificaciones)
            data['total_despues_bonificaciones'] = total_despues_bonificaciones

            # Calcula el total del porcentaje en número
            descuentos = DescuentoNotaVenta.objects.filter(nota_venta=self.nota_venta)
            total_porcentaje = sum(descuento.porcentaje_descuento for descuento in descuentos)
            data['total_porcentaje'] = total_porcentaje

            if self.item_nota_venta:
                self.item_nota_venta.descripcion = ", ".join(self.messages)
                self.item_nota_venta.save()

            return JsonResponse(data, status=200)

        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def add_message(self, message):
        self.messages.append(message)
    def get_messages(self):
        return self.messages if len(self.messages) > 0 else ["Venta registrada exitosamente"]
    
    def caso1(self):
        try:
            articulo = get_object_or_404(Articulo, id=self.id_articulo)
        except Articulo.DoesNotExist:
            return

        promociones = Promocion.objects.filter(
            tipo_promocion='caso_1',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).order_by('cantidad_minima_compra')

        cantidad_bonificada_total = 0

        for promocion in promociones:
            if self.cantidad_comprada >= promocion.cantidad_minima_compra:
                cantidad_bonificada_total += promocion.unidades_bonificadas

        if cantidad_bonificada_total > 0:
            mensaje = f"Por la compra de {self.cantidad_comprada} de {articulo.descripcion}, se bonifican {cantidad_bonificada_total} unidades."
            
            ItemsNotaVenta.objects.create(
                articulo=promocion.articulo_bonificacion,
                nota_venta=self.nota_venta,
                cantidad=cantidad_bonificada_total,
                referencia_bonificacion=self.item_nota_venta,
                descuento_unitario=100,
                es_bonificacion=True,
            )

            self.add_message(mensaje)
        

    def caso2(self):
        promocion = Promocion.objects.filter(
            tipo_promocion='caso_2',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            activo=True
        ).first()

        if promocion:
            proveedor_promocion = promocion.proveedor
            items_proveedor = ItemsNotaVenta.objects.filter(
                nota_venta=self.nota_venta,
                articulo__grupo=proveedor_promocion,
                referencia_bonificacion=self.item_nota_venta,
                es_bonificacion=False  # Excluye los items de bonificación
            )
            total_compra_proveedor = sum(item.total_item for item in items_proveedor)

            if total_compra_proveedor >= promocion.monto_minimo:
                porcentaje_descuento = promocion.porcentaje_descuento
                mensaje = f"Por la compra de S/{total_compra_proveedor:.2f} en productos del proveedor {proveedor_promocion}, se otorga un descuento del {porcentaje_descuento}%."

                # Crear un ítem de bonificación con el descuento
                DescuentoNotaVenta.objects.create(
                    nota_venta=self.nota_venta,
                    porcentaje_descuento=porcentaje_descuento,
                )

                self.add_message(mensaje)
        
    def caso3(self):
        try:
            articulo = Articulo.objects.get(pk=self.id_articulo)
        except Articulo.DoesNotExist:
            return
        promocion_asociada = Promocion_articulos_asociados.objects.filter(
            promocion__tipo_promocion='caso_3',
            promocion__tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo=articulo,
            promocion__activo=True
        ).order_by('-cantidad_articulo').first()
        if promocion_asociada:
            if  promocion_asociada.cantidad_articulo<=self.cantidad_comprada:
                promocion = promocion_asociada.promocion
                porcentaje_descuento = promocion.porcentaje_descuento
                mensaje = f"Por la compra de más de {promocion_asociada.cantidad_articulo} unidades de {articulo.descripcion}, se obtiene un descuento del {porcentaje_descuento}%."
                ItemsNotaVenta.objects.create(
                    articulo=articulo,
                    nota_venta=self.nota_venta,
                    cantidad=self.cantidad_comprada,
                    referencia_bonificacion=self.item_nota_venta,
                    descuento_unitario=porcentaje_descuento,
                    es_bonificacion=True,
                )
                self.add_message(mensaje)        

    def caso4(self):
        try:
            articulo = Articulo.objects.get(pk=self.id_articulo)
        except Articulo.DoesNotExist:
            return

        # Construye la consulta con Q objects
        consulta = Q(
            promocion__tipo_promocion='caso_4',
            promocion__activo=True,
            articulo=articulo
        )

        # Agrega la condición de tipo_cliente si no es nulo
        if self.nota_venta.cliente.canal_cliente:
            consulta &= Q(promocion__tipo_cliente=self.nota_venta.cliente.canal_cliente)
        else:
            consulta &= Q(promocion__tipo_cliente__isnull=True)

        # Obtén todas las promociones que cumplen con la consulta
        promociones_asociadas = Promocion_articulos_asociados.objects.filter(consulta).order_by('-cantidad_articulo')

        for promocion_asociada in promociones_asociadas:
            min = promocion_asociada.promocion.cantidad_minima_compra
            max = promocion_asociada.promocion.cantidad_maxima_compra

            if min <= self.cantidad_comprada <= max:
                porcentaje_descuento = promocion_asociada.promocion.porcentaje_descuento
                mensaje = f"Por la compra de {self.cantidad_comprada} unidades de {articulo.descripcion}, se obtiene un descuento del {porcentaje_descuento}%."
                DescuentoNotaVenta.objects.create(
                    nota_venta=self.nota_venta,
                    porcentaje_descuento=porcentaje_descuento,
                )
                self.add_message(mensaje)
                break  # Si ya se aplicó un descuento, salimos del bucle

    def caso5(self):
        try:
            articulo = Articulo.objects.get(pk=self.id_articulo)
        except Articulo.DoesNotExist:
            return

        promocion = Promocion.objects.filter(
            tipo_promocion='caso_5',
            # tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            importe_compra = self.cantidad_comprada * articulo.precio_unitario
            monto_min = promocion.monto_minimo
            monto_max = promocion.monto_maximo

            if monto_min <= importe_compra <= monto_max:
                porcentaje_descuento = promocion.porcentaje_descuento
                mensaje = f"Por la compra de un importe de S/{importe_compra:.2f} en {articulo.descripcion}, se obtiene un descuento del {porcentaje_descuento}%."
                DescuentoNotaVenta.objects.create(
                    nota_venta=self.nota_venta,
                    porcentaje_descuento=porcentaje_descuento,
                )
                self.add_message(mensaje)

    def caso7(self):
        try:
            articulo = Articulo.objects.get(pk=self.id_articulo)
        except Articulo.DoesNotExist:
            return

        promocion = Promocion.objects.filter(
            tipo_promocion='caso_7',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            cantidad_minima_compra = promocion.cantidad_minima_compra
            unidades_bonificadas = promocion.unidades_bonificadas

            if self.cantidad_comprada >= cantidad_minima_compra:
                mensaje = f"Por la compra de {self.cantidad_comprada} unidades de {articulo.descripcion}, se bonifican {unidades_bonificadas} unidades de {promocion.articulo_bonificacion.descripcion}."
                ItemsNotaVenta.objects.create(
                    articulo=promocion.articulo_bonificacion,
                    nota_venta=self.nota_venta,
                    cantidad=unidades_bonificadas,
                    referencia_bonificacion=self.item_nota_venta,
                    es_bonificacion=True,
                )

                self.add_message(mensaje)

    def caso8(self):
        try:
            articulo = Articulo.objects.get(pk=self.id_articulo)
        except Articulo.DoesNotExist:
            return

        promocion = Promocion.objects.filter(
            tipo_promocion='caso_8',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            cantidad_minima_compra = promocion.cantidad_minima_compra

            if self.cantidad_comprada >= cantidad_minima_compra:
                mensaje = f"Por la compra de {self.cantidad_comprada} unidades de {articulo.descripcion}, se bonifican los siguientes productos:"

                for bonificacion in promocion.promocion_articulos_bonificados.all():
                    ItemsNotaVenta.objects.create(
                        articulo=bonificacion.articulo,
                    descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                        nota_venta=self.nota_venta,
                        cantidad=bonificacion.cantidad_articulo,
                        referencia_bonificacion=self.item_nota_venta,
                        es_bonificacion=True,
                    )

                    mensaje += f" {bonificacion.cantidad_articulo} unidades de {bonificacion.articulo.descripcion},"

                self.add_message(mensaje[:-1])
                
    def caso9(self):
        try:
            articulo = Articulo.objects.get(pk=self.id_articulo)
        except Articulo.DoesNotExist:
            return

        promocion = Promocion.objects.filter(
            tipo_promocion='caso_9',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            importe_compra = self.cantidad_comprada * articulo.precio_unitario

            if promocion.monto_minimo <= importe_compra <= promocion.monto_maximo:
                mensaje = f"Por la compra de un importe de S/{importe_compra:.2f} en {articulo.descripcion}, se obtiene la siguiente promoción combinada:"
                for bonificacion in promocion.promocion_articulos_bonificados.all():
                    ItemsNotaVenta.objects.create(
                        articulo=bonificacion.articulo,
                        nota_venta=self.nota_venta,
                        cantidad=bonificacion.cantidad_articulo,
                        referencia_bonificacion=self.item_nota_venta,
                        descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                        es_bonificacion=True,
                    )
                    mensaje += f" {bonificacion.cantidad_articulo} unidades de {bonificacion.articulo.descripcion},"
                # Descuento
                porcentaje_descuento = promocion.porcentaje_descuento
                mensaje += f" y se aplica un descuento del {porcentaje_descuento}%."
                DescuentoNotaVenta.objects.create(
                    nota_venta=self.nota_venta,
                    porcentaje_descuento=porcentaje_descuento,
                )

                self.add_message(mensaje)

# Vista para obtener los ítems de una nota de venta específica en formato JSON
def obtener_items_nota_venta(request, nota_venta_id):
    # Filtra los ItemsNotaVenta por la nota_venta específica
    items = ItemsNotaVenta.objects.filter(nota_venta__id=nota_venta_id)

    # Construye los datos en el formato requerido por DataTables
    data = [
        {
            'id': item.id,
            'nro_item': item.nro_item,
            'articulo': (
                f"{item.articulo.descripcion} - {item.articulo.unidad_medida.unidad_nombre} "
                f"x {item.articulo.cantidad_unidad_medida} "
            ) if item.articulo and item.articulo.unidad_medida.unidad_nombre == 'paquete' else (
                f"{item.articulo.descripcion} - {item.articulo.unidad_medida.unidad_nombre} "
            ) if item.articulo else '',  # Cambia esto según la estructura real de tu modelo Articulo
            'precio_unitario': item.articulo.precio_unitario,  # Cambia esto según la estructura real de tu modelo Articulo
            'cantidad': item.cantidad,
            'total_item_bruto': float(item.total_item_bruto),
            'factor_descuento': float(item.factor_descuento),
            'descuento_unitario': float(item.descuento_unitario),
            'descripcion': item.descripcion if item.descripcion is not None and item.descripcion != '' else '- -',
            'es_bonificacion': 'Si' if item.es_bonificacion == 1 else 'No',
            'total_item': float(item.total_item),
        }
        for item in items
    ]

    # Crear el diccionario de respuesta con las claves requeridas por DataTables
    response_data = {
        'draw': 0,  # Puedes ajustar esto según tus necesidades
        'recordsTotal': items.count(),
        'recordsFiltered': items.count(),
        'data': data,
    }

    return JsonResponse(response_data)
from django.db.models import Sum

@csrf_exempt
@require_POST
def eliminar_item_nota_venta_api(request, item_id):
    try:
        item = ItemsNotaVenta.objects.get(id=item_id)
        if item:
            # Guarda el descuento antes de eliminar el ítem
            descuentos = DescuentoNotaVenta.objects.filter(nota_venta=item.nota_venta)
            total_descuento = sum(descuento.porcentaje_descuento for descuento in descuentos)

            # Elimina el ítem
            ItemsNotaVenta.objects.filter(referencia_bonificacion=item).delete()
            item.delete()

            # Recalcula el total después de eliminar el ítem
            items_nota_venta_despues_bonificaciones = ItemsNotaVenta.objects.filter(nota_venta=item.nota_venta)
            total_despues_bonificaciones = sum(item.total_item for item in items_nota_venta_despues_bonificaciones)
            value = (float(total_despues_bonificaciones)*(float(total_descuento)/100))-float(total_despues_bonificaciones)


            # Devuelve la respuesta con éxito y la información actualizada
            return JsonResponse({
                'success': True,
                'descuento_total': total_descuento,
                'total_despues_bonificaciones': total_despues_bonificaciones,
                'nuevo_total':value,
            })
    except ItemsNotaVenta.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'El item de la nota de venta no existe'})
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

# Vista basada en función para confirmar una nota de venta por su ID

@api_view(['POST'])
def confirmar_nota_venta(request, nota_venta_id):
    if request.method == 'POST':
        nota_venta = get_object_or_404(NotasVenta, id=nota_venta_id)

        total_pedido = sum(item.total_item for item in nota_venta.itemsnotaventa_set.all())

        nota_venta.total_pedido = total_pedido
        nota_venta.save()

        return JsonResponse({'message': 'Nota de venta confirmada exitosamente', 'total_pedido': total_pedido})

    return JsonResponse({'error': 'Método no permitido'}, status=405)


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Promocion
from .serializers import PromocionSerializer

# Vista basada en clase para activar/inactivar una promoción por su ID

class ActivarInactivarPromocion(APIView):
    def put(self, request, pk):
        promocion = get_object_or_404(Promocion, pk=pk)
        promocion.activo = not promocion.activo  # Cambia el estado de activo a inactivo o viceversa
        promocion.save()

        serializer = PromocionSerializer(promocion)
        return Response(serializer.data)