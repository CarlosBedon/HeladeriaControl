from django.db import models


# Create your models here.
class Product(models.Model):
    # product_id = models.Field(primary_key = True,  null = False)
    presentacion = models.CharField(max_length=200, verbose_name="Tipo de Producto")
    peso = models.PositiveIntegerField(verbose_name="Peso en Gramos")
    precio = models.PositiveIntegerField(verbose_name="Precio", null=True, blank=True)
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

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
    # flavour_id = models.Field(primary_key = True, null = False)
    sabor = models.CharField(max_length=200, verbose_name="Sabor")
    tipo = models.BooleanField(verbose_name="Tipo de Helado Gelato?", null=False, blank=False)
    stock = models.BooleanField(verbose_name="Sabor en Stock en la tienda?", null=False, blank=False)
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Sabor"
        verbose_name_plural = "Sabores"
        ordering = ["-created"]

    def __str__(self):
        return self.sabor
