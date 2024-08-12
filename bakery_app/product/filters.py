from django_filters import FilterSet

from .models import Flavours, Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            "presentacion": ["exact", "contains"],
        }


class FlavourFilter(FilterSet):
    class Meta:
        model = Flavours
        fields = {
            "sabor": ["exact", "contains"],
        }
