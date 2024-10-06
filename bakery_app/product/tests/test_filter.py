import pytest

from bakery_app.product.filters import ProductFilter  # FlavourFilter,
from bakery_app.product.models import MenuHeladeria, ProductosMenu


@pytest.mark.django_db
class TestFilterProduct:
    def test_filter_product(self, products_create):
        product1 = MenuHeladeria.objects.first()
        filter_qs = ProductFilter(data={"productos_menu": product1.productos_menu}).qs
        assert ProductosMenu.objects.count() == 4
        assert filter_qs.count() == 1
        assert filter_qs.first() == product1
