from django.urls import path

from .views import venta

app_name = "venta"
urlpatterns = [
    path("", venta, name="venta"),
]
