import pytest

# from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from bakery_app.product.models import Flavours, Product
from bakery_app.product.views import (  # FlavourCreate, FlavourDelete, FlavourUpdate
    ProductCreate,
    ProductDelete,
    ProductUpdate,
)


@pytest.mark.django_db
def test_Product_View_get_products(client, products_create):
    data = Product.objects.all()
    assert data.count() > 0
    response = client.get(reverse("product:product"))
    assert "Cono Queso" in str(response.content)
    assert "Waffle" in str(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_products__logged(admin_user, rf):
    request = rf.post(
        reverse("product:create"),
        data={
            "presentacion": "Cono",
            "precio": 1.50,
            "peso": 200,
        },
    )
    products_founded = Product.objects.all()
    request.user = admin_user
    response = ProductCreate.as_view()(request)
    assert response.status_code == 302
    assert response.url == "/product/"
    assert products_founded.count() == 1
    assert products_founded.first().presentacion == "Cono"
    assert products_founded.first().precio == 1.50
    assert products_founded.first().peso == 200


@pytest.mark.django_db
def test_create_products__NOT_logged(rf, admin_user):
    request = rf.post(
        reverse("product:create"),
        data={
            "presentacion": "Cono",
            "precio": 1.50,
            "peso": 200,
        },
    )
    products_founded = Product.objects.all()
    # user = admin_user
    response = ProductCreate.as_view()(request)
    assert response.status_code == 302
    assert response.url == "/product/"
    assert products_founded.count() == 0


@pytest.mark.django_db
def test_create_products__invalid(admin_user, rf):
    request = rf.post(
        reverse("product:create"),
        data={
            "presentacion": "Cono",
            "precio": "AA",
            "peso": 200,
        },
    )
    products_founded = Product.objects.all()
    request.user = admin_user
    response = ProductCreate.as_view()(request)
    assert response.status_code == 200
    assert products_founded.count() == 0


@pytest.mark.django_db
def test_update_products_views__access_logged_ussers(client, products_create, django_user_model):
    user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678")
    client.login(username=user.email, password="12345678")
    product = Product.objects.first()
    response = client.get(reverse("product:update", kwargs={"pk": product.pk}))
    assert response.status_code == 200
    assert "Actualizacion de Producto" in str(response.content)
    assert "Precio" in str(response.content)
    assert "Peso" in str(response.content)


@pytest.mark.django_db
def test_update_products__update_data(admin_user, rf, products_create):
    products_founded = Product.objects.all()
    data = Product.objects.first()
    request = rf.post(
        reverse("product:update", kwargs={"pk": data.pk}),
        data={
            "presentacion": "Waffle",
            "precio": 1.00,
            "peso": 100,
        },
    )
    request.user = admin_user
    response = ProductUpdate.as_view()(request, pk=data.pk)
    assert response.status_code == 302
    assert response.url == "/product/?ok"
    assert products_founded.count() == 5
    assert products_founded.first().presentacion == "Waffle"
    assert products_founded.first().precio == 1.00
    assert products_founded.first().peso == 100


@pytest.mark.django_db
def test_delete_products_views(client, admin_user, products_create, django_user_model):
    user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678", is_staff=True)
    client.login(username=user.email, password="12345678")
    product = Product.objects.first()
    response = client.get(reverse("product:delete", kwargs={"pk": product.pk}))
    assert response.status_code == 200
    assert "Eliminar Producto" in str(response.content)
    assert "Estas Seguro de eliminar" in str(response.content)
    assert "Yogurt" in str(response.content)


@pytest.mark.django_db
def test_delete_product(admin_user, rf, products_create):
    data = Product.objects.first()
    products_founded = Product.objects.all()
    inicial_products = products_founded.count()
    request = rf.post(reverse("product:delete", kwargs={"pk": data.pk}))
    request.user = admin_user
    response = ProductDelete.as_view()(request, pk=data.pk)
    products_founded_after_delete = Product.objects.all()
    assert response.status_code == 302
    assert response.url == "/product/?deleted"
    assert inicial_products > products_founded_after_delete.count()


@pytest.mark.django_db
def test_Flavours_View_get_flavours(client, flavours_create):
    data = Flavours.objects.all()
    assert data.count() > 0
    response = client.get(reverse("product:flavour"))
    assert "Mora" in str(response.content)
    assert "Coco" in str(response.content)
    assert response.status_code == 200
