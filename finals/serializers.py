from rest_framework import serializers
from .models import *


class ItemsNotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica el modelo que será serializado
        model = ItemsNotaVenta
        # Indica que se deben incluir todos los campos del modelo en la serialización
        fields = '__all__'

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'
