from django.urls import path

from .views import VentaPageView

app_name = "venta"
urlpatterns = [
    path("", VentaPageView.as_view(), name="venta"),
]
