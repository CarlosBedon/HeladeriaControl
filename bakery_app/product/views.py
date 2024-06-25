from django.shortcuts import render

# from django.views.generic.base import TemplateView


def product(request):
    # return HttpResponse("<h1>HOLAAAA</h1>")
    return render(request, "product/products.html")
