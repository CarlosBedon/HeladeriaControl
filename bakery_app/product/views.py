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


class ProductCreate(CreateView):
    """
    A view for creating a new product.

    This class extends `CreateView` to provide a form for creating a new `Product` instance.
    It handles the creation process and redirects to a specified URL upon successful creation.

    Attributes
    ----------
    model : type
        The model class associated with this view. Must be `Product`.
    fields : list of str
        The fields of the `Product` model that should be included in the form. Includes:
        - "presentacion"
        - "precio"
        - "peso"
    success_url : str
        The URL to redirect to upon successful form submission. Set to the URL pattern named "product:product".
    """

    model = Product
    fields = ["presentacion", "precio", "peso"]
    success_url = reverse_lazy("product:product")


class ProductUpdate(UpdateView):
    """
    A view for updating an existing product.

    This class extends `UpdateView` to provide a form for updating an existing `Product` instance.
    It allows users to modify specified fields and uses a template with a suffix to render the form.
    Upon successful form submission, it redirects to a specified URL with a query parameter.

    Attributes
    ----------
    model : type
        The model class associated with this view. Must be `Product`.
    fields : list of str
        The fields of the `Product` model that should be included in the form. Includes:
        - "presentacion"
        - "precio"
        - "peso"
    template_name_suffix : str
        The suffix to append to the default template name to determine the template used for rendering.
        Defaults to "_update_form", resulting in a template name like "product/product_update_form.html".

    Methods
    -------
    get_success_url()
        Returns the URL to redirect to upon successful form submission, with a query parameter `?ok`.
    """

    model = Product
    fields = ["presentacion", "precio", "peso"]
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


class ProductDelete(DeleteView):
    """
    A view for deleting an existing product.

    This class extends `DeleteView` to handle the deletion of a `Product` instance.
    Upon successful deletion, it redirects to a specified URL with a query parameter.

    Attributes
    ----------
    model : type
        The model class associated with this view. Must be `Product`.

    Methods
    -------
    get_success_url()
        Returns the URL to redirect to upon successful deletion, with a query parameter `?deleted`.
    """

    model = Product

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful deletion of a product.

        This method appends a query parameter `?deleted` to the URL of the view named `"product:product"`,
        indicating that the deletion was successful.

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


class FlavourCreate(CreateView):
    """
    A view for creating a new flavour.

    This class extends `CreateView` to provide a form for creating a new `Flavours` instance.
    It handles the creation process and redirects to a specified URL upon successful creation.

    Attributes
    ----------
    model : type
        The model class associated with this view. Must be `Flavours`.
    fields : list of str
        The fields of the `Flavours` model that should be included in the form. Includes:
        - "sabor"
        - "tipo"
        - "stock"
    success_url : str
        The URL to redirect to upon successful form submission. Set to the URL pattern named "product:flavour".
    """

    model = Flavours
    fields = ["sabor", "tipo", "stock"]
    success_url = reverse_lazy("product:flavour")


class FlavourUpdate(UpdateView):
    """
    A view for updating an existing flavour.

    This class extends `UpdateView` to provide a form for updating an existing `Flavours` instance.
    It allows users to modify specified fields and uses a template with a suffix to render the form.
    Upon successful form submission, it redirects to a specified URL with a query parameter.

    Attributes
    ----------
    model : type
        The model class associated with this view. Must be `Flavours`.
    fields : list of str
        The fields of the `Flavours` model that should be included in the form. Includes:
        - "sabor"
        - "tipo"
        - "stock"
    template_name_suffix : str
        The suffix to append to the default template name to determine the template used for rendering.
        Defaults to "_update_form", resulting in a template name like "flavours/flavour_update_form.html".

    Methods
    -------
    get_success_url()
        Returns the URL to redirect to upon successful form submission, with a query parameter `?ok`.
    """

    model = Flavours
    fields = ["sabor", "tipo", "stock"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful update of a flavour.

        This method appends a query parameter `?ok` to the URL of the view named `"product:flavour"`,
        indicating successful completion of the update.

        Returns
        -------
        str
            The URL to redirect to, with `?ok` appended as a query parameter.
        """
        return reverse_lazy("product:flavour") + "?ok"


class FlavourDelete(DeleteView):
    """
    A view for deleting an existing flavour.

    This class extends `DeleteView` to handle the deletion of a `Flavours` instance.
    Upon successful deletion, it redirects to a specified URL with a query parameter to indicate success.

    Attributes
    ----------
    model : type
        The model class associated with this view. Must be `Flavours`.

    Methods
    -------
    get_success_url()
        Returns the URL to redirect to upon successful deletion, with a query parameter `?deleted`.
    """

    model = Flavours

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful deletion of a flavour.

        This method appends a query parameter `?deleted` to the URL of the view named `"product:flavour"`,
        indicating that the deletion was successful.

        Returns
        -------
        str
            The URL to redirect to, with `?deleted` appended as a query parameter.
        """
        return reverse_lazy("product:flavour") + "?deleted"
