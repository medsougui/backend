from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Producttype
from ..serializers.typeser import ProductTypeSerializer

class ProductTypeList(APIView):
    def get(self, request):
        product_types = Producttype.objects.all()  # Get all product types
        serializer = ProductTypeSerializer(product_types, many=True)
        return Response(serializer.data)
