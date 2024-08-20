from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import FlavourFilter, ProductFilter
from .forms import FlavourFilterFormHelper, FlavourForm, ProductFilterFormHelper, ProductForm
from .models import Flavours, Product
from .tables import FlavoursTable, ProductTable


class StaffRequiredMixin:
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class FilteredSingleTableView(SingleTableMixin, FilterView):
    """
    A view that combines table rendering with filtering capabilities.

    This class extends `SingleTableMixin` and `FilterView` to provide a view that
    integrates table display with filter functionality. It allows for filtering
    table data based on user input.

    Attributes
    ----------
    formhelper_class : type or None
        A class used to customize the form helper for the filter form. If set to `None`,
        the default form helper is used.

    Methods
    -------
    get_filterset(filterset_class)
        Returns an instance of the filterset class with customized form helper.

    """

    formhelper_class = None

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.formhelper_class()
        return filterset


class ProductView(FilteredSingleTableView):
    """
    A view for displaying and filtering products in a paginated table format.

    This class extends `FilteredSingleTableView` to provide a view that renders
    a table of products with filtering and pagination capabilities. It uses a
    specific template and form helper to customize the appearance and functionality
    of the filter form.

    Attributes
    ----------
    template_name : str
        The name of the template to use for rendering the view. Defaults to "product/products.html".
    table_class : type
        The class used to render the table of products. Must be a subclass of `ProductTable`.
    paginate_by : int
        The number of products to display per page. Defaults to 25.
    filterset_class : type
        The filterset class used to filter the products. Must be a subclass of `ProductFilter`.
    formhelper_class : type
        The class used to customize the form helper for the filter form. Defaults to `ProductFilterFormHelper`.
    """

    template_name = "product/products.html"
    table_class = ProductTable
    paginate_by = 25
    filterset_class = ProductFilter
    formhelper_class = ProductFilterFormHelper


class ProductCreate(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:product")


class ProductUpdate(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful form submission.

        This method appends a query parameter `?ok` to the URL of the view named `"product:product"`,
        indicating successful completion of the update.

        Returns
        -------
        str
            The URL to redirect to, with `?ok` appended as a query parameter.
        """
        return reverse_lazy("product:product") + "?ok"


class ProductDelete(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful deletion of a product.

        Returns
        -------
        str
            The URL to redirect to, with `?deleted` appended as a query parameter.
        """
        return reverse_lazy("product:product") + "?deleted"


class FlavourView(FilteredSingleTableView):
    """
    A view for displaying and filtering flavours in a paginated table format.

    This class extends `FilteredSingleTableView` to provide a view that renders
    a table of flavours with filtering and pagination capabilities. It uses a
    specific template and form helper to customize the appearance and functionality
    of the filter form.

    Attributes
    ----------
    template_name : str
        The name of the template to use for rendering the view. Defaults to "product/flavours.html".
    table_class : type
        The class used to render the table of flavours. Must be a subclass of `FlavoursTable`.
    paginate_by : int
        The number of flavours to display per page. Defaults to 25.
    filterset_class : type
        The filterset class used to filter the flavours. Must be a subclass of `FlavourFilter`.
    formhelper_class : type
        The class used to customize the form helper for the filter form. Defaults to `FlavourFilterFormHelper`.
    """

    template_name = "product/flavours.html"
    table_class = FlavoursTable
    paginate_by = 25
    filterset_class = FlavourFilter
    formhelper_class = FlavourFilterFormHelper


class FlavourCreate(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    model = Flavours
    form_class = FlavourForm
    success_url = reverse_lazy("product:flavour")


class FlavourUpdate(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Flavours
    form_class = FlavourForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful update of a flavour.

        Returns
        -------
        str
            The URL to redirect to, with `?ok` appended as a query parameter.
        """
        return reverse_lazy("product:flavour") + "?ok"


class FlavourDelete(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Flavours

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful deletion of a flavour.

        Returns
        -------
        str
            The URL to redirect to, with `?deleted` appended as a query parameter.
        """
        return reverse_lazy("product:flavour") + "?deleted"
