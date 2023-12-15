from rest_framework import serializers
from .models import *


class ItemsNotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsNotaVenta
        fields = '__all__'

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'
