from datetime import timedelta
from itertools import product

from django.db import transaction
from django.utils.timezone import now
from rest_framework import serializers

from inventoryDetails.models import InventoryDetail
from order.models import OrderDetail, Order


class OrderDetailSerializer(serializers.ModelSerializer):
    sub_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity', 'sub_total']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']

        inventory_detail = InventoryDetail.objects.get(product=product)

        if inventory_detail.quantity_in_stock < quantity:
            raise serializers.ValidationError(f'Not enough stock of {product.name}. Available stock is {inventory_detail.quantity_in_stock}')

        data['unit_price'] = product.unit_price
        data['sub_total'] = product.unit_price * quantity
        return data

class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id','order_date', 'customer_id', 'status', 'total_amount', 'details']

    def create(self, validated_data):
        with transaction.atomic():
            details_data = validated_data.pop('details')
            status = validated_data.get('status')

            order = Order.objects.create(**validated_data)

            total_amount = 0
            for detail_data in details_data:
                product = detail_data['product']

                inventory_detail = InventoryDetail.objects.get(product=product)
                if inventory_detail.quantity_in_stock < detail_data['quantity']:
                    raise serializers.ValidationError(f"Not enough stock for product {product.name}")

                order_detail = OrderDetail.objects.create(order=order, **detail_data)
                total_amount += order_detail.sub_total
                if status == 'completed':
                    inventory_detail.quantity_in_stock -= order_detail.quantity
                    inventory_detail.save()
                elif status == 'cancel':
                    raise serializers.ValidationError("Only completed or pending statuses are allowed for create.")
                elif status == 'pending':
                    pass
                else:
                    raise serializers.ValidationError("Invalid status provided.")
            order.total_amount = total_amount
            order.save()
        return order


    def update(self, instance, validated_data):
        with transaction.atomic():

            new_status = validated_data.get('status',instance.status)

            if new_status == 'cancel':

                if now() > instance.order_date + timedelta(days=2):
                    raise serializers.ValidationError("Orders older than 2 days cannot be canceled.")
                for detail in instance.details.all():
                    inventory_detail = InventoryDetail.objects.get(product=detail.product)
                    inventory_detail.quantity_in_stock += detail.quantity
                    inventory_detail.save()
            elif new_status == 'completed':
                for detail in instance.details.all():
                    inventory_detail = InventoryDetail.objects.get(product=detail.product)
                    inventory_detail.quantity_in_stock -= detail.quantity
                    inventory_detail.save()
            else:
                raise serializers.ValidationError("Only completed or canceled statuses are allowed for updates.")
            instance.status = new_status
            instance.save()
        return instance
