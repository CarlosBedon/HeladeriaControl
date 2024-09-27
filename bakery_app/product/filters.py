from django_filters import FilterSet

from .models import FlavoursIceCream, MenuHeladeria


class ProductFilter(FilterSet):
    class Meta:
        model = MenuHeladeria
        fields = {
            "productos_menu": ["exact"],
        }


class FlavourFilter(FilterSet):
    class Meta:
        model = FlavoursIceCream
        fields = {
            "flavour_name": ["exact"],
        }
