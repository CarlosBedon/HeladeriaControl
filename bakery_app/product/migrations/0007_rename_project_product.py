# Generated by Django 4.2.9 on 2024-06-24 15:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_alter_flavours_stock_alter_flavours_tipo"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Project",
            new_name="Product",
        ),
    ]
