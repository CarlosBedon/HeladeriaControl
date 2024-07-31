from django.shortcuts import render  # get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

# from django.views.generic.list import ListView
from django_filters.views import FilterView
from django_tables2 import RequestConfig, SingleTableMixin

from .filters import ProductFilter
from .forms import ProductFilterFormHelper

# from .filters import ProductFilter
# from .forms import ProductForm
from .models import Product
from .tables import ProductTable  # ProductTable1


class ProductPageView(TemplateView):
    template_name = "product/products.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title1": "Productos"})


def testTable(request):
    table = ProductTable(Product.objects.all(), attrs={"class": "paleblue"}, template_name="django_tables2/table.html")
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(request, "product/products.html", {"table": table})


class FilteredProductListView(SingleTableMixin, FilterView):
    table_class = ProductTable
    model = Product
    template_name = "product.html"
    filterset_class = ProductFilter


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
    # def get_success_url(self, **kwargs):
    #    return reverse("product:product")


class ProductUpdate(UpdateView):
    model = Product
    fields = ["presentacion", "precio", "peso"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("product:update", args=[self.object.id]) + "?ok"

    def record(self):
        return self._record
