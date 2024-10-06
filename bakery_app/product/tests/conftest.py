import pytest

from bakery_app.product.tests.factories import FlavourFactory, ProductFactory, ProductosMenuFactory


@pytest.fixture
def one_product_create():
    return ProductFactory.create()


@pytest.fixture
def products_create():
    return ProductFactory.create_batch(4)


@pytest.fixture
def flavours_create():
    return FlavourFactory.create_batch(4)


@pytest.fixture
def create_menu_producto_factory_name():
    return ProductosMenuFactory()


@pytest.fixture
def create_3_menu_producto_factory_name():
    return ProductosMenuFactory.create_batch(3)


@pytest.fixture
def params_menu_products(create_menu_producto_factory_name):
    parametros = {
        "productos_menu": create_menu_producto_factory_name.pk,
        "precio": 1.50,
        "peso_en_helado": 200,
    }
    return parametros


@pytest.fixture
def params_menu_products_update():
    new_product = ProductFactory.create()
    return (
        new_product,
        {
            "productos_menu": new_product.productos_menu.pk,
            "precio": new_product.precio,
            "peso_en_helado": 200,
        },
    )
