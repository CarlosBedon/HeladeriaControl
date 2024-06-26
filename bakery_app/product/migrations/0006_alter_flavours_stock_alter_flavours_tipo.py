# Generated by Django 4.2.9 on 2024-06-20 23:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_alter_flavours_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flavours",
            name="stock",
            field=models.BooleanField(verbose_name="Sabor en Stock en la tienda?"),
        ),
        migrations.AlterField(
            model_name="flavours",
            name="tipo",
            field=models.BooleanField(verbose_name="Tipo de Helado Gelato?"),
        ),
    ]
