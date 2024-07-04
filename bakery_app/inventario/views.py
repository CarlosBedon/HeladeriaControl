from django.views.generic.base import TemplateView


class InventarioPageView(TemplateView):
    template_name = "inventario/stock.html"
