from rest_framework import serializers
from .models import Product, Inventory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    product =  ProductSerializer( read_only=True)
    class Meta:
        model = Inventory
        fields = '__all__'
