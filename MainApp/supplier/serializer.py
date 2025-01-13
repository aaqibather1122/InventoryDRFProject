from rest_framework import serializers

from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name','contact_person', 'email', 'phone_number', 'address', 'created_at', 'updated_at']

    def validate_phone_number(self, value):
        if len(str(value)) != 11:
            raise serializers.ValidationError("Phone number must be 11 digits.")
        return value