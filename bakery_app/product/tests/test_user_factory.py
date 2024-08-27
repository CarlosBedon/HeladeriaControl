import pytest


@pytest.mark.django_db
class TestMyFactoryUser:
    def test_user_user_factory(self, user_factory):
        user = user_factory(name="Juan")
        assert user.name == "Juan"


@pytest.mark.django_db
class TestModelFactory:
    def test_model_factory(self, product_factory):
        Prodcut1 = product_factory(presentacion="Cono")
        assert Prodcut1.presentacion == "Cono"
        print(Prodcut1.peso)
        print(Prodcut1.precio)
