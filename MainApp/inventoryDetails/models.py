from django.db import models

class InventoryDetail(models.Model):
    product = models.OneToOneField('product.Products', on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()
    minimum_stock_level = models.IntegerField()
    reorder_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventory of {self.product.name}"

