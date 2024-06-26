from django.urls import path

from .views import product

app_name = "product"
urlpatterns = [
    path("", product, name="product"),
]
