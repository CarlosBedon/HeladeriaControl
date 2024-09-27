# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import FlavourFilter, ProductFilter
from .forms import FlavourFilterFormHelper, FlavourForm, ProductFilterFormHelper, ProductForm
from .models import FlavoursIceCream, MenuHeladeria
from .tables import FlavoursTable, ProductTable


class FilteredSingleTableView(SingleTableMixin, FilterView):
    formhelper_class = None

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.formhelper_class()
        return filterset


class ProductView(FilteredSingleTableView):
    table_class = ProductTable
    paginate_by = 25
    filterset_class = ProductFilter
    formhelper_class = ProductFilterFormHelper

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product/partials/productshtmx.html"
        else:
            template_name = "product/menuheladeria_filter.html"

        return template_name


class ProductCreate(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = MenuHeladeria
    form_class = ProductForm
    success_url = reverse_lazy("product:product")


class ProductUpdate(
    LoginRequiredMixin,
    UpdateView,
):
    login_url = "/admin/login/"
    redirect_field_name = "login"
    model = MenuHeladeria
    form_class = ProductForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("product:product") + "?ok"


class ProductDelete(LoginRequiredMixin, DeleteView):
    login_url = "/admin/login/"
    model = MenuHeladeria

    def get_success_url(self):
        return reverse_lazy("product:product") + "?deleted"


class FlavourView(FilteredSingleTableView):
    table_class = FlavoursTable
    paginate_by = 25
    filterset_class = FlavourFilter
    formhelper_class = FlavourFilterFormHelper

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product/partials/productshtmx.html"
        else:
            template_name = "product/flavoursicecream_filter.html"

        return template_name


class FlavourCreate(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = FlavoursIceCream
    form_class = FlavourForm
    success_url = reverse_lazy("product:flavour")


class FlavourUpdate(LoginRequiredMixin, UpdateView):
    login_url = "/admin/login/"
    model = FlavoursIceCream
    form_class = FlavourForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("product:flavour") + "?ok"


class FlavourDelete(LoginRequiredMixin, DeleteView):
    login_url = "/admin/login/"
    model = FlavoursIceCream

    def get_success_url(self):
        return reverse_lazy("product:flavour") + "?deleted"
