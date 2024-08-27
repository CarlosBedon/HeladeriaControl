import pytest
from django.urls import reverse

from bakery_app.product.models import Flavours, Product
from bakery_app.product.views import ProductCreate, ProductDelete, ProductUpdate


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
        assert "Cono Doble" in str(response.content)
        assert "Waffle" in str(response.content)
        assert response.status_code == 200


@pytest.mark.django_db
class TestProductCreate:
    def test_login(self, client, django_user_model):
        user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678")
        client.login(username=user.email, password="12345678")
        response = client.get(reverse("product:create"))
        assert response.status_code == 200
        print("STATUS CODE ES")
        print(response.status_code)

    def test_create_products(self, admin_user, rf):
        # view = ProductCreate()
        request = rf.post(
            reverse("product:create"),
            data={
                "presentacion": "Cono",
                "precio": 1.50,
                "peso": 200,
            },
        )
        products_founded = Product.objects.all()
        request.user = admin_user
        response = ProductCreate.as_view()(request)
        assert response.status_code == 302
        assert response.url == "/product/"
        assert products_founded.count() == 1
        assert products_founded.first().presentacion == "Cono"
        assert products_founded.first().precio == 1.50
        assert products_founded.first().peso == 200

    def test_create_products__invalid(self, admin_user, rf):
        # iew = ProductCreate()
        request = rf.post(
            reverse("product:create"),
            data={
                "presentacion": "Cono",
                "precio": "AA",
                "peso": 200,
            },
        )
        products_founded = Product.objects.all()
        request.user = admin_user
        response = ProductCreate.as_view()(request)
        assert response.status_code == 200
        assert products_founded.count() == 0


@pytest.mark.django_db
class TestProductUpdate:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            product1 = Product.objects.create(presentacion="Waffle", peso="150", precio="1.10")
            return product1

        return _data_test

    def test_login(self, client, django_user_model):
        user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678")
        client.login(username=user.email, password="12345678")

    def test_update_products_views(self, client, data_test):
        product = data_test()
        response = client.get(reverse("product:update", kwargs={"pk": product.pk}))
        assert response.status_code == 200
        assert "Actualizacion de Producto" in str(response.content)
        assert "Waffle" in str(response.content)
        assert "Precio" in str(response.content)
        assert "Peso" in str(response.content)

    def test_update_products(self, admin_user, rf, data_test):
        data = data_test()
        # view = ProductUpdate()
        request = rf.post(
            reverse("product:update", kwargs={"pk": data.pk}),
            data={
                "presentacion": "Waffle",
                "precio": 1.00,
                "peso": 100,
            },
        )
        products_founded = Product.objects.all()
        request.user = admin_user
        response = ProductUpdate.as_view()(request, pk=data.pk)
        assert response.status_code == 302
        assert response.url == "/product/?ok"
        assert products_founded.count() == 1
        assert products_founded.first().presentacion == "Waffle"
        assert products_founded.first().precio == 1.00
        assert products_founded.first().peso == 100


@pytest.mark.django_db
class TestProductDelete:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            product_delete = Product.objects.create(presentacion="Yogurt", peso="250", precio="1.00")
            return product_delete

        return _data_test

    def test_login(self, client, django_user_model, data_test):
        user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678")
        client.login(username=user.email, password="12345678")

    def test_delete_products_views(self, client, data_test):
        product = data_test()
        response = client.get(reverse("product:delete", kwargs={"pk": product.pk}))
        assert response.status_code == 200
        assert "Eliminar Producto" in str(response.content)
        assert "Estas Seguro de eliminar" in str(response.content)
        assert "Yogurt" in str(response.content)

    def test_delete_product(self, admin_user, rf, data_test):
        data = data_test()
        # view = ProductDelete()
        request = rf.post(reverse("product:delete", kwargs={"pk": data.pk}))
        products_founded = Product.objects.all()
        request.user = admin_user
        response = ProductDelete.as_view()(request, pk=data.pk)
        assert response.status_code == 302
        assert response.url == "/product/?deleted"
        assert products_founded.count() == 0


@pytest.mark.django_db
class TestFlavourtView:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            flavour1 = Flavours.objects.create(sabor="Mora", tipo="Sorbetto", stock="EN STOCK")
            flavour2 = Flavours.objects.create(sabor="Vainilla", tipo="Gelatto", stock="FUERA DE STOCK")
            return flavour1, flavour2

        return _data_test

    def test_get_flavours(self, client, data_test):
        data = data_test()
        assert str(data[0]) == "Mora"
        assert str(data[1]) == "Vainilla"
        response = client.get(reverse("product:flavour"))
        assert response.status_code == 200
        assert "Sorbetto" in str(response.content)
        assert "FUERA DE STOCK" in str(response.content)


@pytest.mark.django_db
class TestFlavourCreate:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            flavour = Flavours.objects.create(sabor="Mora", tipo="Sorbetto", stock="EN STOCK")
            return flavour

        return _data_test

    def test_create_flavours(self, client, data_test):
        data = data_test()

        assert data.sabor == "Mora"
        response = client.get(reverse("product:flavourCreate"))
        assert response.status_code == 200
        assert "Agrega el Sabor" in str(response.content)
        assert "Sabor" in str(response.content)
        assert "Stock" in str(response.content)
        assert "Tipo" in str(response.content)


@pytest.mark.django_db
class TestFlavourtUpdate:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            flavour = Flavours.objects.create(sabor="Mora", tipo="Sorbetto", stock="EN STOCK")
            return flavour

        return _data_test

    def test_update_update_views(self, client, data_test):
        data = data_test()

        assert str(data) == "Mora"
        response = client.get(reverse("product:flavourUpdate", kwargs={"pk": data.pk}))
        assert response.status_code == 200
        assert "Actualizacion de Sabor" in str(response.content)
        assert "Sabor" in str(response.content)
        assert "Stock" in str(response.content)
        assert "Tipo" in str(response.content)
        assert "Mora" in str(response.content)
        assert "Sorbetto" in str(response.content)
        assert "EN STOCK" in str(response.content)


@pytest.mark.django_db
class TestFlavourDelete:
    @pytest.fixture
    def data_test(self):
        def _data_test():
            flavour = Flavours.objects.create(sabor="Banana", tipo="Gelatto", stock="FUERA DE STOCK")
            return flavour

        return _data_test

    def test_delete_flavour_views(self, client, data_test):
        data = data_test()

        assert str(data) == "Banana"
        response = client.get(reverse("product:flavourDelete", kwargs={"pk": data.pk}))
        assert response.status_code == 200
        assert "Eliminar Sabor" in str(response.content)
        assert "Estas Seguro de eliminar el Helado Sabor a" in str(response.content)
        assert "Banana" in str(response.content)
