import django_tables2 as tables

from .models import Product


class ProductTable(tables.Table):
    presentacion = tables.Column()
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

    #   summary = tables.Column(order_by=("presentacion", "precio"))
    class Meta:
        model = Product
        exclude = ("created",)


class ProductBootstrapTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "presentacion", "peso", "precio")
        linkify = ("presentacion", "peso")


class ProductBootstrap5Table(tables.Table):
    Product = tables.Column(linkify=True)
    #    continent = tables.Column(accessor="country__continent", linkify=True)

    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap5.html"
