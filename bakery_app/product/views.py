from django.views.generic.base import TemplateView


class ProductPageView(TemplateView):
    template_name = "product/products.html"
