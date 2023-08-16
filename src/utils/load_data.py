import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import csv
from datetime import datetime
from src.client.models import Client
from src.branch.models import BranchOffice
from src.product.models import Product, Inventory
from decimal import Decimal

csv_file_path = '../../data.csv'


def load_data():
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        column_names = [column.strip() for column in csv_reader.fieldnames]

        for row in csv_reader:
            precio_unidad = Decimal(row['PrecioUnidad'].replace(',', '.'))
            fecha_inventario = datetime.strptime(row['FechaInventario'], '%d/%m/%y')
            gln_cliente = row['GLN_Cliente']
            gln_sucursal = row['GLN_Sucrusal']
            gtin_producto = row['Gtin_Producto']
            inventario_final = int(row['Inventario_Final'])

            # Obtener o crear instancias de Client, BranchOffice y Product
            client, _ = Client.objects.get_or_create(GLN_Client=gln_cliente)
            branch_office, _ = BranchOffice.objects.get_or_create(GLN_sucursal=gln_sucursal)
            product, _ = Product.objects.get_or_create(Gtin_Producto=gtin_producto)
            product.price = precio_unidad

            product.save()

            # Crear la entrada en Inventory
            inventory_entry = Inventory(
                client=client,
                branch_office=branch_office,
                product=product,
                quantity=inventario_final,
                inventory_date=fecha_inventario
            )
            inventory_entry.save()


load_data()
