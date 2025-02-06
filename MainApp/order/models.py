from django.db import models

from customer.models import Customer


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(choices=[('pending', 'Pending'), ('cancel', 'Cancel'), ('completed', 'Completed')], max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='details',on_delete=models.CASCADE)
    product = models.ForeignKey('product.Products',on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.sub_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)

