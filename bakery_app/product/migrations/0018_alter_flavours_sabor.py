# Generated by Django 4.2.9 on 2024-09-13 04:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0017_alter_flavours_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flavours",
            name="sabor",
            field=models.CharField(max_length=200, unique=True, verbose_name="Sabor"),
        ),
    ]