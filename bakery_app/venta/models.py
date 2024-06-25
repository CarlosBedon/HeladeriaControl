from django.db import models


# Create your models here.
class VentasDiarias(models.Model):
    Kind_of_Product = models.CharField(max_length=200, verbose_name="Tipode Producto")
    Price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio")
    # image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Registro Inicial")

    class Meta:
        verbose_name = "Venta Diaria"
        verbose_name_plural = "Ventas Diarias"
        ordering = ["-Kind_of_Product"]

    def __str__(self):
        return self.Kind_of_Product
