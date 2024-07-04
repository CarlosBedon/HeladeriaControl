from django.views.generic.base import TemplateView


class InicioPageView(TemplateView):
    template_name = "pages/inicio.html"
