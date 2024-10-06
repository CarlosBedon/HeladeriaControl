import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import FlavourFilter, ProductFilter
from .forms import FlavourFilterFormHelper, FlavourForm, ProductFilterFormHelper, ProductForm
from .models import FlavoursIceCream, MenuHeladeria
from .tables import FlavoursTable, ProductTable


class SaveMixin:
    def form_valid(self, form):
        form.save()
        return HttpResponse(status=204, headers={"HX-Trigger": json.dumps({"update_table": None})})


class DeleteMixin:
    def form_valid(self, form):
        self.object.delete()
        return HttpResponse(status=204, headers={"HX-Trigger": json.dumps({"update_table": None})})


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


class ProductCreate(LoginRequiredMixin, SaveMixin, CreateView):
    login_url = "/admin/login/"
    model = MenuHeladeria
    form_class = ProductForm

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class ProductUpdate(
    LoginRequiredMixin,
    SaveMixin,
    UpdateView,
):
    login_url = "/admin/login/"
    redirect_field_name = "login"
    model = MenuHeladeria
    form_class = ProductForm
    template_name_suffix = "_update_form"

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class ProductDelete(DeleteMixin, DeleteView):
    login_url = "/admin/login/"
    model = MenuHeladeria


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


class FlavourCreate(LoginRequiredMixin, SaveMixin, CreateView):
    login_url = "/admin/login/"
    model = FlavoursIceCream
    form_class = FlavourForm
    success_url = reverse_lazy("product:flavour")


class FlavourUpdate(LoginRequiredMixin, SaveMixin, UpdateView):
    login_url = "/admin/login/"
    model = FlavoursIceCream
    form_class = FlavourForm
    template_name_suffix = "_update_form"


class FlavourDelete(LoginRequiredMixin, DeleteMixin, DeleteView):
    login_url = "/admin/login/"
    model = FlavoursIceCream
