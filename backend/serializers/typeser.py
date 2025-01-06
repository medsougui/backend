from rest_framework import serializers
from ..models import Producttype

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producttype
        fields = ['id', 'name']