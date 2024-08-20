from django.urls import path

from .views import (
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
    path("create/", ProductCreate.as_view(), name="create"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", ProductDelete.as_view(), name="delete"),
    path("", ProductView.as_view(), name="product"),
    path("flavour", FlavourView.as_view(), name="flavour"),
    path("flavour/create/", FlavourCreate.as_view(), name="flavourCreate"),
    path("flavour/update/<int:pk>/", FlavourUpdate.as_view(), name="flavourUpdate"),
    path("flavour/delete/<int:pk>/", FlavourDelete.as_view(), name="flavourDelete"),
]
