from django.urls import path

from .views import FilteredProductListView, ProductCreate, ProductUpdate  # ProductPageView

app_name = "product"
urlpatterns = [
    path("", FilteredProductListView.as_view(), name="product"),
    path("create/", ProductCreate.as_view(), name="create"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="update"),
    # path("", testTable, name="product"),
    # path("table/", testTable, name="testTable"),
]
