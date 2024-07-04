# Generated by Django 4.2.9 on 2024-06-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResumenPesoHelado",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start_total_weight", models.PositiveIntegerField(verbose_name="Peso Total_Inicial")),
                ("end_total_weight", models.PositiveIntegerField(verbose_name="Peso Total_Final")),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Fecha")),
                ("Total_Weight_Selled", models.PositiveIntegerField(verbose_name="Total_Vendido")),
            ],
            options={
                "verbose_name": "Peso Global",
                "verbose_name_plural": "Pesos Globales",
                "ordering": ["-date"],
            },
        ),
        migrations.DeleteModel(
            name="Resumen",
        ),
    ]