from itertools import product

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Products
from .models import InventoryDetail
from .serializer import InventoryDetailSerializer

class InventoryList(APIView):
    def get(self,request):
        inventory = InventoryDetail.objects.all()
        serializer = InventoryDetailSerializer(inventory,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = InventoryDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class InventoryCheckView(APIView):
    def get(self,request, product_id):
        try:
            inventory = InventoryDetail.objects.get(product_id=product_id)

            if inventory.quantity_in_stock <= inventory.minimum_stock_level:
                return Response({
                    'message' : f'Stock for product {inventory.product.name} is below minimum. Reorder {inventory.reorder_quantity} units.',
                    'reorder-quantity' : inventory.reorder_quantity,
                    'current_stock': inventory.quantity_in_stock
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': f"Stock for product '{inventory.product.name}' is sufficient.",
                    'current_stock': inventory.quantity_in_stock
                }, status=status.HTTP_200_OK)

        except InventoryDetail.DoesNotExist:
            return Response({
                'error': 'Inventory details not found for the provided product ID.'
            }, status=status.HTTP_404_NOT_FOUND)


    def post(self,request,product_id):
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({'Message' : 'Product Not Found'},status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['product'] = product.id

        serializer = InventoryDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryEdit(APIView):
    def get(self,request,product_id):
        try:
            inventory = InventoryDetail.objects.get(product_id=product_id)
            serializer = InventoryDetailSerializer(inventory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except InventoryDetail.DoesNotExist:
            return Response({"error": "Inventory details not found for the specified product"},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self,request,product_id):
        try:
            inventory = InventoryDetail.objects.get(product_id=product_id)
        except InventoryDetail.DoesNotExist:
            return Response({"error": "Inventory detail not found for the specified product"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = InventoryDetailSerializer(inventory,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, product_id):
        try:
            inventory = InventoryDetail.objects.get(product_id=product_id)
        except InventoryDetail.DoesNotExist:
            return Response({"error": "Inventory detail not found for the specified product"},
                            status=status.HTTP_404_NOT_FOUND)

        inventory.delete()
        return Response({"message": "Inventory detail deleted successfully"}, status=status.HTTP_204_NO_CONTENT)