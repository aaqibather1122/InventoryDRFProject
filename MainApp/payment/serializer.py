from django.conf import settings
from rest_framework import serializers
import stripe
from payment.models import Payment



class PaymentIntentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=3, required=False, default='usd')

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    