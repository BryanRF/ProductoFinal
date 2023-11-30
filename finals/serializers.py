from rest_framework import serializers, viewsets
from .models import ItemsNotaVenta


class ItemsNotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsNotaVenta
        fields = '__all__'
