from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.http import JsonResponse

from .models import *
from .serializers import *

from django.shortcuts import render
from django.http import JsonResponse
from .models import Promocion, Promocion_articulos_asociados, Promocion_articulos_bonificados
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

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
            id_articulo = request.data.get('articulo')
            cantidad_comprada = self.serializer.validated_data['cantidad']
            self.nota_venta = NotasVenta.objects.get(pk=request.data.get('nota_venta'))
            
            self.caso1(id_articulo, cantidad_comprada)
            self.caso2(id_articulo, cantidad_comprada)
            # Unir los mensajes en una cadena antes de asignarlos a 'descripcion'
            self.serializer.validated_data['descripcion'] = ", ".join(self.messages)
            

            data = {'message':  self.get_messages(), 'status':self.serializer.validated_data['es_bonificacion']}
            self.serializer.save()
            return JsonResponse(data, status=200)
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def add_message(self, message):
        self.messages.append(message)
    def get_messages(self):
        return self.messages if len(self.messages) > 0 else ["Venta registrada exitosamente"]
    
    def caso1(self, id_articulo, cantidad_comprada):
        bonificacion = self.calcular_bonificacion(id_articulo, cantidad_comprada)
        self.serializer.validated_data['es_bonificacion'] = '1' if bonificacion > 0 else '0'
    def calcular_bonificacion(self, id_articulo, cantidad_comprada):
        articulo = Articulo.objects.get(pk=id_articulo)
        if articulo.codigo_sku == '203101':
            articulo_value = Articulo.objects.get(codigo_sku='200101B')
            if cantidad_comprada == 48:
                ItemsNotaVenta.objects.create(
                    articulo=articulo_value,
                    nota_venta= self.nota_venta,
                    cantidad=2,  
                    descripcion=f'Bonificacion por la compra de 48 {articulo.descripcion}',
                    descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                    es_bonificacion=1,  # No es una bonificación según la solicitud
                )
                self.add_message(f"Tu venta a sido bonificada con 2 {articulo_value.descripcion}")
                return 1
            else:
                return 0
        else:
            return 0
        
    def caso2(self, id_articulo, cantidad_comprada):
        bonificacion = self.calcular_bonificacion(id_articulo, cantidad_comprada)
        self.serializer.validated_data['es_bonificacion'] = '1' if bonificacion > 0 else '0'
    def calcular_bonificacion(self, id_articulo, cantidad_comprada):
        articulo = Articulo.objects.get(pk=id_articulo)
        if articulo.codigo_sku == '203101':
            articulo_value = Articulo.objects.get(codigo_sku='200101B')
            if cantidad_comprada == 48:
                ItemsNotaVenta.objects.create(
                    articulo=articulo_value,
                    nota_venta= self.nota_venta,
                    cantidad=2,  
                    descripcion=f'Bonificacion por la compra de 48 {articulo.descripcion}',
                    descuento_unitario=100,  # Ajusta el descuento unitario según sea necesario
                    es_bonificacion=1,  # No es una bonificación según la solicitud
                )
                self.add_message(f"Tu venta a sido bonificada con 2 {articulo_value.descripcion}")
                return 1
            else:
                return 0
        else:
            return 0
        
        
        
    
