from datetime import datetime

from factory import Faker, Iterator, SubFactory
from factory.django import DjangoModelFactory

from bakery_app.product.models import FlavourName, FlavoursIceCream, MenuHeladeria, ProductosMenu


class ProductosMenuFactory(DjangoModelFactory):
    class Meta:
        model = ProductosMenu

    productos_menu = Faker("pystr", max_chars=6)


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = MenuHeladeria

    productos_menu = SubFactory(ProductosMenuFactory)
    peso_en_helado = Faker("pyint", min_value=50, max_value=300)
    precio = Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    created = Faker(
        "date_between", start_date=datetime(year=2024, month=1, day=1).date(), end_date=datetime.now().date()
    )
    updated = Faker("date_between", start_date=created, end_date=datetime.now().date())


class FlavourNameFactory(DjangoModelFactory):
    class Meta:
        model = FlavourName

    flavour_name = Faker("pystr", max_chars=6)


class FlavourFactory(DjangoModelFactory):
    class Meta:
        model = FlavoursIceCream

    flavour_name = SubFactory(FlavourNameFactory)
    tipo = Iterator([x[0] for x in FlavoursIceCream.TYPE_ICE_CREAM])
    stock = Iterator([x[0] for x in FlavoursIceCream.STOCK_FLAVOUR])
    created = Faker(
        "date_between", start_date=datetime(year=2024, month=1, day=1).date(), end_date=datetime.now().date()
    )
    updated = Faker("date_between", start_date=created, end_date=datetime.now().date())
