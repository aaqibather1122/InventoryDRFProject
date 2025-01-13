from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'created_at', 'updated_at']


    def validate_phone_number(self,value):
        if len(str(value)) != 11:
            raise serializers.ValidationError("Phone number must be 11 digits.")
        return value