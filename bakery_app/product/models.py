from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    # product_id = models.Field(primary_key = True,  null = False)
    presentacion = models.CharField(max_length=200, verbose_name="Tipo de Producto")
    peso = models.PositiveIntegerField(verbose_name="Peso")
    precio = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Precio",
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modificado el")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created"]

    def __str__(self):
        return self.presentacion

    @property
    def summary(self):
        return f"{self.presentacion} (pop. {self.precio})"


class Flavours(models.Model):
    sabor = models.CharField(max_length=200, verbose_name="Sabor")
    TYPE_ICE_CREAM = (
        ("1", "Gelatto"),
        ("2", "Sorbetto"),
    )
    tipo = models.CharField(max_length=200, verbose_name="Tipo", choices=TYPE_ICE_CREAM)
    STOCK_FLAVOUR = (
        ("1", "EN STOCK"),
        ("2", "FUERA DE STOCK"),
    )
    stock = models.CharField(verbose_name="Stock", null=False, blank=False, choices=STOCK_FLAVOUR)
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Sabor"
        verbose_name_plural = "Sabores"
        ordering = ["-created"]

    def __str__(self):
        return self.sabor
