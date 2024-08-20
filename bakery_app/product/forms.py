from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from .models import Flavours, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["presentacion", "peso", "precio"]
        readonly_fields = ["created", "updated"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Guardar"))
        self.helper.layout = Layout(
            "presentacion",
            Row(
                Column("peso", css_class="form-group col-md-6 mb-0"),
                Column("precio", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "updated",
            "created",
        )


class ProductFilterFormHelper(FormHelper):
    form_method = "GET"
    layout = Layout(
        Row(
            Column("presentacion", css_class="form-group col-md-10 mb-5"),
            Column(Submit("submit", "Buscar"), css_class="form-group col-md-2 mb-5"),
            css_class="form-row",
        )
    )


class FlavourForm(forms.ModelForm):
    class Meta:
        model = Flavours
        fields = ["sabor", "tipo", "stock"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Guardar"))
        self.helper.layout = Layout(
            "sabor",
            Row(
                Column("tipo", css_class="form-group col-md-5 mb-0"),
                Column("stock", css_class="form-group col-md-7 mb-0"),
                css_class="form-row",
            ),
        )


class FlavourFilterFormHelper(FormHelper):
    form_method = "GET"
    layout = Layout(
        Row(
            Column("sabor", css_class="form-group col-md-10 mb-5"),
            Column(Submit("submit", "Buscar"), css_class="form-group col-md-2 mb-5"),
            css_class="form-row",
        )
    )
