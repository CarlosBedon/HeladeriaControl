# Generated by Django 4.2.9 on 2024-08-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0015_alter_flavours_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flavours",
            name="stock",
            field=models.CharField(choices=[("1", "EN STOCK"), ("2", "FUERA DE STOCK")], verbose_name="Stock"),
        ),
    ]
