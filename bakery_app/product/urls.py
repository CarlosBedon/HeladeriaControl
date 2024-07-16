from django.urls import path

from .views import testTable  # ProductPageView

app_name = "product"
urlpatterns = [
    path("", testTable, name="product"),
    # path("table/", testTable, name="testTable"),
]
