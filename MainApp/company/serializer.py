import re

from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'phone_number', 'email', 'supplier','created_at', 'updated_at','owner']

    def validate_phone_number(self, value):
        if not re.match(r'^\d{11,13}$', value):
            raise serializers.ValidationError("Phone number must be between 11 and 13 digits.")
        return value

    def validate_name(self, value):
        if self.instance:
            if Company.objects.exclude(id=self.instance.id).filter(name=value).exists():
                raise serializers.ValidationError("Company name already exists.")
        else:
            if Company.objects.filter(name=value).exists():
                raise serializers.ValidationError("Company name already exists.")
        return value

    def validate_email(self, value):
        if self.instance:
            if Company.objects.exclude(id=self.instance.id).filter(email=value).exists():
                raise serializers.ValidationError("Email already exists.")
        else:
            if Company.objects.filter(email=value).exists():
                raise serializers.ValidationError("Email already exists.")
        return value
