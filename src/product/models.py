from django.db import models
from src.client.models import Client
from src.branch.models import BranchOffice


# Create your models here.

class Product(models.Model):
    Gtin_Producto = models.CharField(max_length=13, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'nexos_product'


class Inventory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField()
    inventory_date = models.DateField()

    class Meta:
        db_table = 'nexos_inventory'
