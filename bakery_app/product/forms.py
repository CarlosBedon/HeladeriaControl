from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from .models import Flavours, Product


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ["presentacion", "peso", "precio", "updated"]


class ProductFilterFormHelper(FormHelper):
    form_method = "GET"
    layout = Layout(
        "presentacion",
        Submit("submit", "Buscar"),
    )


class FlavourForm(forms.Form):
    class Meta:
        model = Flavours
        fields = ["sabor", "tipo", "stock"]


class FlavourFilterFormHelper(FormHelper):
    form_method = "GET"
    layout = Layout(
        "sabor",
        Submit("submit", "Buscar"),
    )
