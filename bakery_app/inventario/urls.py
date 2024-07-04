from django.urls import path

from .views import InventarioPageView

app_name = "stock"

urlpatterns = [
    path("", InventarioPageView.as_view(), name="stock"),
]
