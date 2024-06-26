from django.urls import path

from .views import stock

app_name = "stock"

urlpatterns = [
    path("", stock, name="stock"),
]
