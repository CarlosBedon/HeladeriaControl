from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django_tables2 import RequestConfig

# from .filters import ProductFilter
from .forms import ProductForm
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


class ProductListView(ListView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
