import pytest

from bakery_app.product.tests.factories import FlavourFactory, ProductFactory


@pytest.fixture
def products_create():
    return ProductFactory.create_batch(5)


@pytest.fixture
def flavours_create():
    return FlavourFactory.create_batch(5)
