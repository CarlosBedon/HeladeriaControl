import pytest
from django.urls import reverse

from bakery_app.product.models import Product


@pytest.mark.django_db
class TestProductView:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            product1 = Product.objects.create(presentacion="Waffle", peso="150", precio="1.10")
            product2 = Product.objects.create(presentacion="Cono Doble", peso="200", precio="2.10")
            return product1, product2

        return _data_test

    def test_get_products(self, client, data_test):
        data = data_test()
        # import ipdb
        # ipdb.set_trace()
        assert str(data[0]) == "Waffle"
        assert str(data[1]) == "Cono Doble"
        response = client.get(reverse("product:product"))
        assert response.status_code == 200
        assert "Cono Doble" in str(response.content)
        assert "Waffle" in str(response.content)


@pytest.mark.django_db
class TestProductCreate:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            product_new = Product.objects.create(presentacion="Cono Doble", peso="180", precio="1.50")
            return product_new

        return _data_test

    def test_create_products(self, client, data_test):
        data = data_test()

        assert data.presentacion == "Cono Doble"
        response = client.get(reverse("product:create"))
        assert response.status_code == 200
        assert "Agrega el Producto" in str(response.content)
        assert "Tipo de Producto" in str(response.content)
        assert "Precio" in str(response.content)
        assert "Peso" in str(response.content)


@pytest.mark.django_db
class TestProductUpdate:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            product_update = Product.objects.create(presentacion="Yogurt", peso="250", precio="1.00")
            return product_update

        return _data_test

    def test_update_products_views(self, client, data_test):
        data = data_test()

        assert str(data) == "Yogurt"
        response = client.get(reverse("product:update", kwargs={"pk": data.pk}))
        assert response.status_code == 200
        assert "Actualizacion de Producto" in str(response.content)
        assert "Tipo de Producto" in str(response.content)
        assert "Precio" in str(response.content)
        assert "Peso" in str(response.content)
