from rest_framework import serializers
from ..models import Products
import base64

class ProductSerializer(serializers.ModelSerializer):
    image_base64 = serializers.SerializerMethodField()  # Add a custom field for the Base64 image
    class Meta:
        model = Products
        fields = ['idp', 'name', 'price', 'description', 'sales', 'nbstock', 'image_base64','type']
    def get_image_base64(self, obj):
        if obj.photo:
            # Encode the binary data into a Base64 string
            return f"data:image/jpeg;base64,{base64.b64encode(obj.photo).decode('utf-8')}"
        return None  # Return None if no image is present
