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
def promocion_list_create(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
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

            return JsonResponse({'message': 'Promoción creada exitosamente', 'ok':True}, status=201)
    except Exception as e:
            return JsonResponse({'message': f'Error al procesar la solicitud: {str(e)}', 'ok':False}, status=500)

    return JsonResponse({'message': 'Método no permitido', 'ok':False}, status=405)




class ItemsNotaVentaAPIView(APIView):
    def __init__(self, *args, **kwargs):
        super(ItemsNotaVentaAPIView, self).__init__(*args, **kwargs)
        self.messages = []
        self.nota_venta= None
        self.serializer= None
        
    def post(self, request, *args, **kwargs):
        self.serializer = ItemsNotaVentaSerializer (data=request.data)
        if self.serializer.is_valid():
            self.serializer.save()
            id_articulo = request.data.get('articulo')
            cantidad_comprada = self.serializer.validated_data['cantidad']
            self.nota_venta = NotasVenta.objects.get(pk=request.data.get('nota_venta'))
            self.caso1(id_articulo, cantidad_comprada)
            self.caso2(id_articulo, cantidad_comprada)
            self.caso3(id_articulo, cantidad_comprada)
            self.caso4(id_articulo, cantidad_comprada)
            self.caso5(id_articulo, cantidad_comprada)
            self.caso7(id_articulo, cantidad_comprada)
            self.caso8(id_articulo, cantidad_comprada)
            self.caso9(id_articulo, cantidad_comprada)
            self.serializer.validated_data['descripcion'] = ", ".join(self.messages)
            data = {'message':  self.get_messages()}
            self.serializer.save()
            return JsonResponse(data, status=200)
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def add_message(self, message):
        self.messages.append(message)
    def get_messages(self):
        return self.messages if len(self.messages) > 0 else ["Venta registrada exitosamente"]
    
    def caso1(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
        except Articulo.DoesNotExist:
            return
        promocion = Promocion.objects.filter(
            tipo_promocion='caso_1',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            if promocion.cantidad_minima_compra >= cantidad_comprada:
                cantidad_bonificada = promocion.unidades_bonificadas
                mensaje= f"Tu venta ha sido bonificada con {cantidad_bonificada} {promocion.articulo_bonificacion.descripcion}"
                ItemsNotaVenta.objects.create(
                    articulo=promocion.articulo_bonificacion,
                    nota_venta=self.nota_venta,
                    cantidad=cantidad_bonificada,
                    descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                    es_bonificacion=True,
                )
                self.add_message(mensaje)
        
    def caso2(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
        except Articulo.DoesNotExist:
            return
        promocion = Promocion.objects.filter(
            tipo_promocion='caso_2',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            proveedor=articulo.grupo,  #busca por proveedor
            activo=True
        ).first()

        if promocion :
            if promocion.monto_minimo >= (cantidad_comprada * articulo.precio_unitario):
                porcentaje_descuento = promocion.porcentaje_descuento
                descuento_monto = cantidad_comprada * articulo.precio_unitario * (porcentaje_descuento / 100)
                mensaje = f"Por la compra de S/{cantidad_comprada * articulo.precio_unitario:.2f} en productos del proveedor {articulo.grupo}, se otorga un descuento del {porcentaje_descuento}%."
                ItemsNotaVenta.objects.create(
                    articulo=articulo,
                    nota_venta=self.nota_venta,
                    cantidad=cantidad_comprada,
                    descuento_unitario=porcentaje_descuento,
                    es_bonificacion=True,
                )
                self.add_message(mensaje)
        
    def caso3(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
        except Articulo.DoesNotExist:
            return
        promocion_asociada = Promocion_articulos_asociados.objects.filter(
            promocion__tipo_promocion='caso_3',
            promocion__tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo=articulo,
            promocion__activo=True
        ).order_by('-cantidad_articulo').first()
        if promocion_asociada:
            if  promocion_asociada.cantidad_articulo<=cantidad_comprada:
                promocion = promocion_asociada.promocion
                porcentaje_descuento = promocion.porcentaje_descuento
                descuento_monto = cantidad_comprada * articulo.precio_unitario * (porcentaje_descuento / 100)
                mensaje = f"Por la compra de más de {promocion_asociada.cantidad_articulo} unidades de {articulo.descripcion}, se obtiene un descuento del {porcentaje_descuento}%."
                ItemsNotaVenta.objects.create(
                    articulo=articulo,
                    nota_venta=self.nota_venta,
                    cantidad=cantidad_comprada,
                    descuento_unitario=porcentaje_descuento,
                    es_bonificacion=True,
                )
                self.add_message(mensaje)        
    def caso4(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
        except Articulo.DoesNotExist:
            return
        promocion_asociada = Promocion_articulos_asociados.objects.filter(
            promocion__tipo_promocion='caso_4',
            articulo=articulo,
            promocion__activo=True
        ).order_by('-cantidad_articulo').first()
        
        if promocion_asociada :
            min = promocion_asociada.promocion.cantidad_minima_compra
            max = promocion_asociada.promocion.cantidad_minima_compra
            if (min <= cantidad_comprada <= max):
                porcentaje_descuento = promocion_asociada.promocion.porcentaje_descuento
                descuento_monto = cantidad_comprada * articulo.precio_unitario * (porcentaje_descuento / 100)
                mensaje = f"Por la compra de {cantidad_comprada} unidades de {articulo.descripcion}, se obtiene un descuento del {porcentaje_descuento}%."
                ItemsNotaVenta.objects.create(
                    articulo=articulo,
                    nota_venta=self.nota_venta,
                    cantidad=cantidad_comprada,
                    descuento_unitario=porcentaje_descuento,
                    es_bonificacion=True,
                )
                self.add_message(mensaje)
    def caso5(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
        except Articulo.DoesNotExist:
            return

        promocion = Promocion.objects.filter(
            tipo_promocion='caso_5',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            importe_compra = cantidad_comprada * articulo.precio_unitario
            monto_min = promocion.monto_minimo
            monto_max = promocion.monto_maximo

            if monto_min <= importe_compra <= monto_max:
                porcentaje_descuento = promocion.porcentaje_descuento
                descuento_monto = importe_compra * (porcentaje_descuento / 100)
                mensaje = f"Por la compra de un importe de S/{importe_compra:.2f} en {articulo.descripcion}, se obtiene un descuento del {porcentaje_descuento}%."
                ItemsNotaVenta.objects.create(
                    articulo=articulo,
                    nota_venta=self.nota_venta,
                    cantidad=cantidad_comprada,
                    descuento_unitario=porcentaje_descuento,
                    es_bonificacion=True,
                )
                self.add_message(mensaje)

    def caso7(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
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

            if cantidad_comprada >= cantidad_minima_compra:
                mensaje = f"Por la compra de {cantidad_comprada} unidades de {articulo.descripcion}, se bonifican {unidades_bonificadas} unidades de {promocion.articulo_bonificacion.descripcion}."
                ItemsNotaVenta.objects.create(
                    articulo=promocion.articulo_bonificacion,
                    nota_venta=self.nota_venta,
                    cantidad=unidades_bonificadas,
                    es_bonificacion=True,
                )

                self.add_message(mensaje)

    def caso8(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
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

            if cantidad_comprada >= cantidad_minima_compra:
                mensaje = f"Por la compra de {cantidad_comprada} unidades de {articulo.descripcion}, se bonifican los siguientes productos:"

                for bonificacion in promocion.promocion_articulos_bonificados.all():
                    ItemsNotaVenta.objects.create(
                        articulo=bonificacion.articulo,
                    descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                        nota_venta=self.nota_venta,
                        cantidad=bonificacion.cantidad_articulo,
                        es_bonificacion=True,
                    )

                    mensaje += f" {bonificacion.cantidad_articulo} unidades de {bonificacion.articulo.descripcion},"

                self.add_message(mensaje[:-1])
                
    def caso9(self, id_articulo, cantidad_comprada):
        try:
            articulo = Articulo.objects.get(pk=id_articulo)
        except Articulo.DoesNotExist:
            return

        promocion = Promocion.objects.filter(
            tipo_promocion='caso_9',
            tipo_cliente=self.nota_venta.cliente.canal_cliente,
            articulo_aplicable=articulo,
            activo=True
        ).first()

        if promocion:
            importe_compra = cantidad_comprada * articulo.precio_unitario

            if promocion.monto_minimo <= importe_compra <= promocion.monto_maximo:
                mensaje = f"Por la compra de un importe de S/{importe_compra:.2f} en {articulo.descripcion}, se obtiene la siguiente promoción combinada:"
                for bonificacion in promocion.promocion_articulos_bonificados.all():
                    ItemsNotaVenta.objects.create(
                        articulo=bonificacion.articulo,
                        nota_venta=self.nota_venta,
                        cantidad=bonificacion.cantidad_articulo,
                    descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                        es_bonificacion=True,
                    )
                    mensaje += f" {bonificacion.cantidad_articulo} unidades de {bonificacion.articulo.descripcion},"
                # Descuento
                porcentaje_descuento = promocion.porcentaje_descuento
                descuento_monto = importe_compra * (porcentaje_descuento / 100)
                mensaje += f" y se aplica un descuento del {porcentaje_descuento}%."
                ItemsNotaVenta.objects.create(
                    articulo=articulo,
                    nota_venta=self.nota_venta,
                    cantidad=cantidad_comprada,
                    descuento_unitario=porcentaje_descuento,
                    es_bonificacion=True,
                )

                self.add_message(mensaje)

def obtener_items_nota_venta(request, nota_venta_id):
    # Filtra los ItemsNotaVenta por la nota_venta específica
    items = ItemsNotaVenta.objects.filter(nota_venta__id=nota_venta_id)

    # Construye los datos en el formato requerido por DataTables
    data = [
        {
            'id': item.id,
            'nro_item': item.nro_item,
            'articulo': item.articulo.descripcion,  # Cambia esto según la estructura real de tu modelo Articulo
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
@csrf_exempt  # Esto es solo para este ejemplo, asegúrate de manejar la protección CSRF de manera adecuada en un entorno de producción
@require_POST
def eliminar_item_nota_venta_api(request, item_id):
    try:
        item = ItemsNotaVenta.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'success': True})
    except ItemsNotaVenta.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'El item de la nota de venta no existe'})
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

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

class ActivarInactivarPromocion(APIView):
    def put(self, request, pk):
        promocion = get_object_or_404(Promocion, pk=pk)
        promocion.activo = not promocion.activo  # Cambia el estado de activo a inactivo o viceversa
        promocion.save()

        serializer = PromocionSerializer(promocion)
        return Response(serializer.data)