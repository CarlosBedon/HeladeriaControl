# from collections.abc import Sequence

# from factory import Faker, post_generation
from factory import Faker
from factory.django import DjangoModelFactory

# import bakery_app.product.tests.factories as factories
from bakery_app.product.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    presentacion = Faker("name")
    peso = Faker("pyint", min_value=50, max_value=300)
    precio = Faker("pyfloat", min_value=1.0, max_value=5.0)
