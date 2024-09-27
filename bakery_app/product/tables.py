# import django_tables2 as tables
from django_tables2 import Column, Table, TemplateColumn

from .models import FlavoursIceCream, MenuHeladeria


class ProductTable(Table):
    id = Column()
    productos_menu = Column(accessor="productos_menu", verbose_name="Productos del Menu")
    peso_en_helado = Column(verbose_name="Peso de la Bola de Helado")
    precio = Column()
    created = Column()
    updated = Column()
    button_edit = TemplateColumn(template_name="product/edit_buttons.html", verbose_name=("Editar"), orderable=False)
    button_delete = TemplateColumn(
        template_name="product/delete_buttons.html", verbose_name=("Eliminar"), orderable=False
    )

    class Meta:
        model = MenuHeladeria
        exclude = ("created",)


class FlavoursTable(Table):
    id = Column()
    flavour_name = Column(accessor="flavour_name", verbose_name="Sabor de Helado")
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
        model = FlavoursIceCream
        exclude = ("created", "updated")
