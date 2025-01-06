import base64
from rest_framework import serializers
from ..models import AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'  # Include all fields from the AuthUser model