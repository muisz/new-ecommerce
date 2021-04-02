from rest_framework import serializers
from ..models.product import Shops

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'