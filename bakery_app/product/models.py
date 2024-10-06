from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class ProductosMenu(models.Model):
    productos_menu = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Menu Producto"
        verbose_name_plural = "Menu Productos"

    def __str__(self):
        return self.productos_menu


class MenuHeladeria(models.Model):
    productos_menu = models.ForeignKey(ProductosMenu, on_delete=models.CASCADE)
    peso_en_helado = models.PositiveIntegerField(verbose_name="Peso en Helado")
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
        verbose_name = "Menu Heladeria"
        verbose_name_plural = "Menu Heladeria"
        ordering = ["-created"]

    def __str__(self):
        return str(self.productos_menu)


class FlavourName(models.Model):
    flavour_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Sabor Helado"
        verbose_name_plural = "Sores Helados"

    def __str__(self):
        return self.flavour_name


class FlavoursIceCream(models.Model):
    flavour_name = models.ForeignKey(FlavourName, on_delete=models.CASCADE)
    TYPE_ICE_CREAM = (
        ("1", "Gelatto"),
        ("2", "Sorbetto"),
    )
    tipo = models.CharField(max_length=10, verbose_name="Tipo", choices=TYPE_ICE_CREAM)
    STOCK_FLAVOUR = (
        ("1", "SI"),
        ("2", "NO"),
    )
    stock = models.CharField(verbose_name="En Stock", null=False, blank=False, choices=STOCK_FLAVOUR)
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Helado"
        verbose_name_plural = "Helados"
        ordering = ["-created"]

    def __str__(self):
        return str(self.flavour_name)
