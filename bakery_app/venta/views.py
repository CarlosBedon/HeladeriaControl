from django.views.generic.base import TemplateView


class VentaPageView(TemplateView):
    template_name = "venta/venta.html"
