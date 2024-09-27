import pytest
from django.urls import resolve, reverse, reverse_lazy

from bakery_app.product.models import Flavours, Product


def test_product_view():
    assert reverse_lazy("product:product") == "/product/"
    assert resolve("/product/").view_name == "product:product"


def test_product_create():
    assert reverse("product:create") == "/product/create/"
    assert resolve("/product/create/").view_name == "product:create"


@pytest.mark.django_db
def test_product_update(products_create):
    product = Product.objects.first()
    assert reverse("product:update", kwargs={"pk": product.pk}) == f"/product/update/{product.pk}/"
    assert resolve(f"/product/update/{product.pk}/").view_name == "product:update"


@pytest.mark.django_db
def test_product_delete(products_create):
    product = Product.objects.first()
    assert reverse("product:delete", kwargs={"pk": product.pk}) == f"/product/delete/{product.pk}/"
    assert resolve(f"/product/delete/{product.pk}/").view_name == "product:delete"


def test_flavour_view():
    assert reverse_lazy("product:flavour") == "/product/flavour"
    assert resolve("/product/flavour").view_name == "product:flavour"


def test_flavour_create():
    assert reverse("product:flavourCreate") == "/product/flavour/create/"
    assert resolve("/product/flavour/create/").view_name == "product:flavourCreate"


@pytest.mark.django_db
def test_flavour_update(flavours_create):
    flavour = Flavours.objects.first()
    assert reverse("product:flavourUpdate", kwargs={"pk": flavour.pk}) == f"/product/flavour/update/{flavour.pk}/"
    assert resolve(f"/product/flavour/update/{flavour.pk}/").view_name == "product:flavourUpdate"


@pytest.mark.django_db
def test_flavour_delete(flavours_create):
    flavour = Flavours.objects.first()
    assert reverse("product:flavourDelete", kwargs={"pk": flavour.pk}) == f"/product/flavour/delete/{flavour.pk}/"
    assert resolve(f"/product/flavour/delete/{flavour.pk}/").view_name == "product:flavourDelete"
