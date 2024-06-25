from django.contrib import admin

from .models import EndDay, StartDay


# Register your models here.
@admin.register(StartDay)
class CheckInAdmin(admin.ModelAdmin):
    readonly_fields = ["check_in"]  # CAMPOS DE SOLO LECTURA


@admin.register(EndDay)
class CheckOutAdmin(admin.ModelAdmin):
    readonly_fields = ["check_out"]  # CAMPOS DE SOLO LECTURA
