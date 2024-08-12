# Generated by Django 4.2.9 on 2024-08-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0013_alter_flavours_stock_alter_flavours_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flavours",
            name="tipo",
            field=models.CharField(choices=[("1", "Gelato"), ("2", "Sorbetto")], max_length=200, verbose_name="Tipo"),
        ),
    ]