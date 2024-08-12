# import django_tables2 as tables
from django_tables2 import Column, Table, TemplateColumn

from .models import Flavours, Product


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


class FlavoursTable(Table):
    id = Column()
    sabor = Column(accessor="sabor", verbose_name="Sabor")
    tipo = Column(verbose_name="Tipo")
    stock = Column(verbose_name="Stock")
    created = Column()
    updated = Column()
    button_edit = TemplateColumn(
        template_name="product/edit_buttons_flavour.html", verbose_name=("Editar"), orderable=False
    )
    button_delete = TemplateColumn(
        template_name="product/delete_buttons_flavour.html", verbose_name=("Eliminar"), orderable=False
    )

    class Meta:
        model = Flavours
        exclude = ("created", "updated")
