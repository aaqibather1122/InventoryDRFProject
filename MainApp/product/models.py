from tkinter.constants import CASCADE

from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100,unique=True)
    company = models.ForeignKey('company.Company',on_delete=models.CASCADE,related_name='products')
    supplier = models.ForeignKey('supplier.Supplier' ,on_delete=models.SET_NULL,null=True,related_name='supplier')
    unit_price = models.DecimalField(decimal_places=2,max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.sku}"

