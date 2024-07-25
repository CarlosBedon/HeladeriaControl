from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

# from django.views.generic.list import ListView
from django_filters.views import FilterView
from django_tables2 import RequestConfig, SingleTableMixin

from .filters import ProductFilter

# from .filters import ProductFilter
# from .forms import ProductForm
from .models import Product
from .tables import ProductTable


class ProductPageView(TemplateView):
    template_name = "product/products.html"

    #   def get_context_data(self, **kwargs):
    #       context = super().get_context_data(**kwargs)
    #       context['title1'] = "Productos"
    #       return context
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title1": "Productos"})


def testTable(request):
    table = ProductTable(Product.objects.all(), attrs={"class": "paleblue"}, template_name="django_tables2/table.html")
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(request, "product/products.html", {"table": table})


# CLASE PARA FILTROS
class FilteredProductListView(SingleTableMixin, FilterView):
    table_class = ProductTable
    model = Product
    template_name = "product.html"
    filterset_class = ProductFilter


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

    def get_success_url(self, **kwargs):
        return reverse_lazy("product:update", args=[self.get_object.id])
