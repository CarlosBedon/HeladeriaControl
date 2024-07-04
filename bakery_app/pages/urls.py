from django.urls import path

from .views import InicioPageView

app_name = "inicio"
urlpatterns = [
    path("", InicioPageView.as_view(), name="inicio"),
]
