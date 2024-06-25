from django.urls import path

from .views import venta

urlpatterns = [
    path("", venta, name="venta"),
]
