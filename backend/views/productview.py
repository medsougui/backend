from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Products
from ..serializers.productser import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        products = Products.objects.all()  # Get all products from the table
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
