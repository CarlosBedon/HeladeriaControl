# Generated by Django 4.2.9 on 2024-06-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VentasDiarias",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("Kind_of_Product", models.CharField(max_length=200, verbose_name="Tipode Producto")),
                ("Price", models.PositiveIntegerField(verbose_name="Precio")),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Registro Inicial")),
            ],
            options={
                "verbose_name": "Venta Diaria",
                "verbose_name_plural": "Ventas Diarias",
                "ordering": ["-Kind_of_Product"],
            },
        ),
    ]