from django.db import models


# Create your models here.

class BranchOffice(models.Model):
    GLN_sucursal = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'nexos_branch_office'
