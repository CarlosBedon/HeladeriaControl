import pytest
from django.urls import resolve, reverse, reverse_lazy

from bakery_app.product.models import Product


def test_view():
    assert reverse_lazy("product:product") == "/product/"
    assert resolve("/product/").view_name == "product:product"


def test_create():
    assert reverse("product:create") == "/product/create/"
    assert resolve("/product/create/").view_name == "product:create"


@pytest.mark.django_db
def test_update():
    product = Product.objects.create(presentacion="Cono", peso="150", precio="1.10")
    assert reverse("product:update", kwargs={"pk": product.pk}) == f"/product/update/{product.pk}/"
    assert resolve(f"/product/update/{product.pk}/").view_name == "product:update"


@pytest.mark.django_db
def test_delete():
    product = Product.objects.create(presentacion="Cono", peso="150", precio="1.10")
    assert reverse("product:delete", kwargs={"pk": product.pk}) == f"/product/delete/{product.pk}/"
    assert resolve(f"/product/delete/{product.pk}/").view_name == "product:delete"
