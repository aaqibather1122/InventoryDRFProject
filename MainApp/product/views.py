from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Products
from .serializer import ProductSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
