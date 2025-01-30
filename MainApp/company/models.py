from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.SET_NULL, null=True, related_name='supplier')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
