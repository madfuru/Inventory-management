from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    class meta:
        verbose_name_plural = 'Product ff'

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.Product} orderd by {self.staff.username}'