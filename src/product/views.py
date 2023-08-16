from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Inventory
from .serializers import InventorySerializer
from rest_framework import status



class InventoryList(APIView):
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)


