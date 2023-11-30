from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import ItemsNotaVenta,Articulo,NotasVenta
from .serializers import ItemsNotaVentaSerializer

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
        
        
        
    
