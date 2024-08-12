from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import FlavourFilter, ProductFilter
from .forms import FlavourFilterFormHelper, ProductFilterFormHelper
from .models import Flavours, Product
from .tables import FlavoursTable, ProductTable


# CLASE PARA FILTROS
class FilteredSingleTableView(SingleTableMixin, FilterView):
    formhelper_class = None

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.formhelper_class()
        return filterset


# MODEL VIEW
class ProductView(FilteredSingleTableView):
    template_name = "product/products.html"
    table_class = ProductTable
    paginate_by = 25
    filterset_class = ProductFilter
    formhelper_class = ProductFilterFormHelper


class ProductCreate(CreateView):
    model = Product
    fields = ["presentacion", "precio", "peso"]
    success_url = reverse_lazy("product:product")


class ProductUpdate(UpdateView):
    model = Product
    fields = ["presentacion", "precio", "peso"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("product:product") + "?ok"


class ProductDelete(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy("product:product") + "?deleted"


class FlavourView(FilteredSingleTableView):
    template_name = "product/flavours.html"
    table_class = FlavoursTable
    paginate_by = 25
    filterset_class = FlavourFilter
    formhelper_class = FlavourFilterFormHelper


class FlavourCreate(CreateView):
    model = Flavours
    fields = ["sabor", "tipo", "stock"]
    success_url = reverse_lazy("product:flavour")
