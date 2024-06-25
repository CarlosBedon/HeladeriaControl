# from datetime import datetime

from django.db import models


# Create your models here.
class StartDay(models.Model):
    flavour = models.CharField(max_length=200, verbose_name="Sabor del Helado", unique_for_date="check_in")
    start_weight = models.PositiveIntegerField(verbose_name="Peso Inicial")
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    check_in = models.DateTimeField(auto_now_add=True, verbose_name="Registro Inicial")
    comments = models.TextField(verbose_name="Comentarios", null=True, blank=True)

    class Meta:
        verbose_name = "Registro Entrada"
        verbose_name_plural = "Registros Entrada"
        ordering = ["-flavour"]

    def __str__(self):
        return self.flavour


class EndDay(models.Model):
    flavour = models.CharField(max_length=200, verbose_name="Sabor del Helado", unique_for_date="check_in")
    end_weight = models.PositiveIntegerField(verbose_name="Peso Cierre")
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    check_out = models.DateTimeField(auto_now_add=True, verbose_name="Registro Cierre")
    comments = models.TextField(verbose_name="Comentarios", null=True, blank=True)

    class Meta:
        verbose_name = "Registro Salida"
        verbose_name_plural = "Registros Salida"
        ordering = ["-flavour"]

    def __str__(self):
        return self.flavour
