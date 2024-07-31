from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from .models import Product


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ["presentacion", "peso", "precio"]


class ProductFilterFormHelper(FormHelper):
    form_method = "GET"
    layout = Layout(
        "presentacion",
        Submit("submit", "Buscar"),
    )
