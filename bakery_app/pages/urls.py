from django.urls import path

from .views import inicio

app_name = "inicio"
urlpatterns = [
    path("", inicio, name="inicio"),
]
