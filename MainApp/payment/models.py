from django.db import models

from order.models import Order


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('cash', 'Cash'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    order = models.ForeignKey('order.Order',on_delete=models.CASCADE,related_name='payments')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    amount_return = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    stripe_payment_intent_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.payment_method == 'cash' and self.amount_received > self.total_amount:
            self.amount_return = self.amount_received - self.total_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.payment_status}"