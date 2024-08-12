import pytest
from django.urls import reverse

from bakery_app.product.models import Product

# from bakery_app.product.views import ProductView


@pytest.fixture
def data_test():
    def _data_test():
        product1 = Product.objects.create(presentacion="Waffle", peso="150", precio="1.10")
        product2 = Product.objects.create(presentacion="Cono Doble", peso="200", precio="2.10")
        return product1, product2

    return _data_test


class Test_Product_View:
    def test_get_products(self, client, data_test):
        data = data_test()

        assert data.product1.presentacion == "Waffle"
        assert data.product2.presentacion == "Cono Doble"
        response = client.get(reverse("product:product"))
        assert response.status_code == 200
        assert "Cono Doble" in str(response.content)
        assert "Waffle" in str(response.content)
