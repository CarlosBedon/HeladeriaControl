import pytest

from bakery_app.product.models import Product


@pytest.mark.django_db
class Test_Producto:
    def test_create_product(self):
        producto = Product.objects.create(
            presentacion="Cono Simple",
            peso="200",
            precio="1.20",
        )
        assert producto.presentacion == "Cono Simple"
        assert producto.precio == "1.20"
        assert producto.peso == "200"
        assert float(producto.precio) >= 0.0
        assert int(producto.peso) >= 0
