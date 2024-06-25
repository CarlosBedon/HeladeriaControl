from django.urls import path

from .views import product

# from .views import ProductPageView, InicioPageView

# urlpatterns = [
#    path('product/', ProductPageView.as_view(),name='product'),
#    path('inicio/', InicioPageView.as_view(),name='inicio'),
# ]

urlpatterns = [
    path("", product, name="product"),
]
