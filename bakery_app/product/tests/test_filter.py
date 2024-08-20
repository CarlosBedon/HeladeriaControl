import pytest

from bakery_app.product.filters import ProductFilter  # FlavourFilter,
from bakery_app.product.models import Product  # Flavours,


@pytest.mark.django_db
class TestFilterProduct:
    def test_filter_product(self):
        product1 = Product.objects.create(presentacion="Cono", peso="200", precio="1.50")
        product2 = Product.objects.create(presentacion="Waffle", peso="100", precio="1.00")

        filter_qs = ProductFilter(data={"presentacion": "Cono"}).qs
        filter_qs_2 = ProductFilter(data={"presentacion": "Waffle"}).qs
        # import ipdb
        # ipdb.set_trace()
        assert filter_qs.count() == 1
        assert filter_qs.first() == product1
        assert filter_qs_2.count() == 1
        assert filter_qs_2.first() == product2
