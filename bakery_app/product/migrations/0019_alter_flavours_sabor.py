# Generated by Django 4.2.9 on 2024-09-20 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0018_alter_flavours_sabor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flavours",
            name="sabor",
            field=models.CharField(max_length=200, verbose_name="Sabor"),
        ),
    ]
