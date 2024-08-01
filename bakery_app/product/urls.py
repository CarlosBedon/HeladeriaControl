from django.urls import path

from .views import ProductCreate, ProductDelete, ProductUpdate, ProductView  # ProductPageView,FilteredProductListView,

app_name = "product"
urlpatterns = [
    # path("", FilteredProductListView.as_view(), name="product"),
    path("create/", ProductCreate.as_view(), name="create"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", ProductDelete.as_view(), name="delete"),
    path("", ProductView.as_view(), name="product"),
]
