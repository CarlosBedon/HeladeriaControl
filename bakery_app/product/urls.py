from django.urls import path

from .views import ProductPageView

app_name = "product"
urlpatterns = [
    path("", ProductPageView.as_view(), name="product"),
]
