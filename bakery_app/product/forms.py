from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row, Submit
from django import forms

from .models import FlavoursIceCream, MenuHeladeria


class ProductForm(forms.ModelForm):
    class Meta:
        model = MenuHeladeria
        fields = ["productos_menu", "peso_en_helado", "precio"]
        readonly_fields = ["created", "updated"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Guardar"))
        self.helper.layout = Layout(
            "productos_menu",
            Row(
                Column(Field("peso_en_helado"), css_class="form-group col-md-6 mb-0"),
                Column("precio", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
        )


class ProductFilterFormHelper(FormHelper):
    form_method = "GET"
    layout = Layout(
        Row(
            Column("productos_menu", css_class="form-group col-md-10 mb-5"),
            Column(Submit("submit", "Buscar"), css_class="form-group col-md-2 mb-5"),
            css_class="form-row",
        )
    )


class FlavourForm(forms.ModelForm):
    class Meta:
        model = FlavoursIceCream
        fields = ["flavour_name", "tipo", "stock"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Guardar"))
        self.helper.layout = Layout(
            "flavour_name",
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
            Column("flavour_name", css_class="form-group col-md-10 mb-5"),
            Column(Submit("submit", "Buscar"), css_class="form-group col-md-2 mb-5"),
            css_class="form-row",
        )
    )
