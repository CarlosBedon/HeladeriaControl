from django.shortcuts import render

# Create your views here.


def stock(request):
    return render(request, "inventario/stock.html")
