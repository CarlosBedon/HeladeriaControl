import django_tables2 as tables
from django_tables2 import Column, Table, TemplateColumn

from .models import Product


class ProductTable1(tables.Table):
    id = tables.Column()
    presentacion = tables.Column(accessor="presentacion", verbose_name="Presentacion")
    peso = tables.Column(verbose_name="Peso Sugerido")
    precio = tables.Column()
    created = tables.Column()
    updated = tables.Column()
    button_edit = tables.TemplateColumn(
        template_name="product/edit_buttons.html", verbose_name=("Editar"), orderable=False
    )
    button_delete = tables.TemplateColumn(
        template_name="product/delete_buttons.html", verbose_name=("Eliminar"), orderable=False
    )

    class Meta:
        model = Product
        exclude = ("created",)


class ProductTable(Table):
    id = Column()
    presentacion = Column(accessor="presentacion", verbose_name="Presentacion")
    peso = Column(verbose_name="Peso Sugerido")
    precio = Column()
    created = Column()
    updated = Column()
    button_edit = TemplateColumn(template_name="product/edit_buttons.html", verbose_name=("Editar"), orderable=False)
    button_delete = TemplateColumn(
        template_name="product/delete_buttons.html", verbose_name=("Eliminar"), orderable=False
    )

    class Meta:
        model = Product
        exclude = ("created",)
