from django.contrib import admin

from .models import VentasDiarias


# Register your models here.
# Register your models here.
@admin.register(VentasDiarias)
class VentasAdmin(admin.ModelAdmin):
    readonly_fields = ["date"]  # CAMPOS DE SOLO LECTURA
