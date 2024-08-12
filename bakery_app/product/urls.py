from django.urls import path

from .views import (  # ProductPageView,FilteredProductListView,
    FlavourCreate,
    FlavourDelete,
    FlavourUpdate,
    FlavourView,
    ProductCreate,
    ProductDelete,
    ProductUpdate,
    ProductView,
)

app_name = "product"
urlpatterns = [
    # path("", FilteredProductListView.as_view(), name="product"),
    path("create/", ProductCreate.as_view(), name="create"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", ProductDelete.as_view(), name="delete"),
    path("", ProductView.as_view(), name="product"),
    # FlavoursURLS
    path("flavour", FlavourView.as_view(), name="flavour"),
    path("flavourCreate/", FlavourCreate.as_view(), name="flavourCreate"),
    path("flavourUpdate/<int:pk>/", FlavourUpdate.as_view(), name="flavourUpdate"),
    path("flavourDelete/<int:pk>/", FlavourDelete.as_view(), name="flavourDelete"),
]
