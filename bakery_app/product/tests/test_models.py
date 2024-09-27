# import datetime

import pytest

from bakery_app.product.models import Flavours, Product


@pytest.mark.django_db
def test_create_product(products_create):
    productos = Product.objects.all()
    assert productos.count() > 0


@pytest.mark.django_db
def test_create_product_positive_price_show_raisen_error(products_create):
    producto = Product.objects.all()
    for price in producto:
        assert float(price.precio) > 0.0


@pytest.mark.django_db
def test_create_date_update_date(products_create):
    producto = Product.objects.all()
    for t in producto:
        print(t.created)
        assert t.created <= t.updated


@pytest.mark.django_db
def test_create_flavour(flavours_create):
    flavour = Flavours.objects.all()
    assert flavour.count() > 0
