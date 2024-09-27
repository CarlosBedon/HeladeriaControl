from django.contrib import admin

from .models import FlavourName, FlavoursIceCream, MenuHeladeria, ProductosMenu

# Register your models here.
admin.site.register(MenuHeladeria)
admin.site.register(FlavoursIceCream)
admin.site.register(FlavourName)
admin.site.register(ProductosMenu)
