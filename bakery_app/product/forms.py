from django import forms


class ProductForm(forms.Form):
    presentacion = forms.CharField(label="Producto en Venta", max_length=200, required=True)
    peso = forms.DecimalField(label="Peso Bola Helado", max_digits=4, required=True)
    precio = forms.DecimalField(label="Precio", max_digits=6, decimal_places=2, required=True)
    created = forms.DateField(label="Fecha de Implementacion", required=True, widget=forms.SelectDateWidget)
