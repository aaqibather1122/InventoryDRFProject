from rest_framework import serializers

from .models import InventoryDetail


class InventoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryDetail
        fields = ['id', 'product', 'quantity_in_stock', 'minimum_stock_level', 'reorder_quantity', 'created_at', 'updated_at']