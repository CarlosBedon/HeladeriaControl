import django_tables2 as tables

from .models import Product


class ProductTable(tables.Table):
    presentacion = tables.Column()
    peso = tables.Column(verbose_name="Peso Sugerido")
    precio = tables.Column()
    created = tables.Column()
    updated = tables.Column()

    #   summary = tables.Column(order_by=("presentacion", "precio"))
    class Meta:
        model = Product
