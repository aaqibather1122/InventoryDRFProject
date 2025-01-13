from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Supplier
from .serializer import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


