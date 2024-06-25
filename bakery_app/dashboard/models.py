# from datetime import datetime

from django.db import models


class ResumenPesoHelado(models.Model):
    start_total_weight = models.PositiveIntegerField(verbose_name="Peso Total_Inicial")
    end_total_weight = models.PositiveIntegerField(verbose_name="Peso Total_Final")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    total_weight_selled = models.PositiveIntegerField(verbose_name="Total_Vendido")

    class Meta:
        verbose_name = "Peso Global"
        verbose_name_plural = "Pesos Globales"
        ordering = ["-date"]

    def __str__(self):
        return self.total_weight_selled
