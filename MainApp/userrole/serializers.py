from rest_framework import serializers

from .Models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','role', 'created_at', 'updated_at']

