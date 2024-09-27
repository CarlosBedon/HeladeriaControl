from datetime import datetime

from factory import Faker, Iterator
from factory.django import DjangoModelFactory

from bakery_app.product.models import Flavours, Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    presentacion = Iterator(["Cono", "Waffle", "Tulipan", "Cono Queso", "Yogurt"])
    peso = Faker("pyint", min_value=50, max_value=300)
    precio = Faker("pyfloat", min_value=1.0, max_value=5.0)
    created = Faker(
        "date_between", start_date=datetime(year=2024, month=1, day=1).date(), end_date=datetime.now().date()
    )
    updated = Faker("date_between", start_date=created, end_date=datetime.now().date())


class FlavourFactory(DjangoModelFactory):
    class Meta:
        model = Flavours

    sabor = Iterator(["Mora", "Chocolate", "Vainilla", "Fresa", "Coco"])
    tipo = Iterator([x[0] for x in Flavours.TYPE_ICE_CREAM])
    stock = Iterator([x[0] for x in Flavours.STOCK_FLAVOUR])
    created = Faker(
        "date_between", start_date=datetime(year=2024, month=1, day=1).date(), end_date=datetime.now().date()
    )
    updated = Faker("date_between", start_date=created, end_date=datetime.now().date())
