from django.db import models

class Role(models.Model):
    ROLE_CHOICE = [
        ('admin','Admin'),
        ('manager','Manager'),
        ('staff','Staff')
    ]
    role = models.CharField(max_length=100,choices=ROLE_CHOICE)
    description = models.TextField()

    def __str__(self):
        return self.role
