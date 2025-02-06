import re

from rest_framework import serializers

from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_person', 'email', 'phone_number', 'address', 'created_at', 'updated_at']

    def validate_phone_number(self, value):
        if not re.match(r'^\d{11,13}$', value):
            raise serializers.ValidationError("Phone number must be between 11 and 13 digits.")
        return value