from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    """
    Represents a product in the inventory.

    Attributes
    ----------
    presentacion : CharField
        The type or presentation of the product, with a maximum length of 200 characters.
    peso : PositiveIntegerField
        The weight of the product, stored as a positive integer.
    precio : DecimalField, optional
        The price of the product, with a maximum of 6 digits in total and 2 decimal places.
        Can be null or blank, and has a minimum value validator set to 0.00.
    created : DateTimeField
        The date and time when the product was created, automatically set on creation.
    updated : DateTimeField
        The date and time when the product was last updated, automatically updated on save.
    """

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
    """
    Represents a flavour of ice cream.

    Attributes
    ----------
    sabor : CharField
        The taste or flavour of the ice cream, with a maximum length of 200 characters.
    tipo : CharField
        The type of ice cream, chosen from predefined options (e.g., Gelatto or Sorbetto).
        Options include:
        - "1" for Gelatto
        - "2" for Sorbetto
    stock : CharField
        The stock status of the flavour, chosen from predefined options (e.g., in stock or out of stock).
        Options include:
        - "1" for EN STOCK
        - "2" for FUERA DE STOCK
    created : DateTimeField
        The date and time when the flavour was created, automatically set on creation.
    updated : DateTimeField
        The date and time when the flavour was last updated, automatically updated on save.
    """

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
