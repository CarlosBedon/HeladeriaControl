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
def test_product_update():
    product = Product.objects.create(presentacion="Cono", peso="150", precio="1.10")
    assert reverse("product:update", kwargs={"pk": product.pk}) == f"/product/update/{product.pk}/"
    assert resolve(f"/product/update/{product.pk}/").view_name == "product:update"


@pytest.mark.django_db
def test_product_delete():
    product = Product.objects.create(presentacion="Cono", peso="150", precio="1.10")
    assert reverse("product:delete", kwargs={"pk": product.pk}) == f"/product/delete/{product.pk}/"
    assert resolve(f"/product/delete/{product.pk}/").view_name == "product:delete"


def test_flavour_view():
    assert reverse_lazy("product:flavour") == "/product/flavour"
    assert resolve("/product/flavour").view_name == "product:flavour"


def test_flavour_create():
    assert reverse("product:flavourCreate") == "/product/flavourCreate/"
    assert resolve("/product/flavourCreate/").view_name == "product:flavourCreate"


@pytest.mark.django_db
def test_flavour_update():
    flavour = Flavours.objects.create(sabor="Banana", tipo="Gelatto", stock="FUERA DE STOCK")
    assert reverse("product:flavourUpdate", kwargs={"pk": flavour.pk}) == f"/product/flavourUpdate/{flavour.pk}/"
    assert resolve(f"/product/flavourUpdate/{flavour.pk}/").view_name == "product:flavourUpdate"


@pytest.mark.django_db
def test_flavour_delete():
    flavour = Flavours.objects.create(sabor="Banana", tipo="Gelatto", stock="FUERA DE STOCK")
    assert reverse("product:flavourDelete", kwargs={"pk": flavour.pk}) == f"/product/flavourDelete/{flavour.pk}/"
    assert resolve(f"/product/flavourDelete/{flavour.pk}/").view_name == "product:flavourDelete"
