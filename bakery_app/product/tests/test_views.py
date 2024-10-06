from decimal import Decimal

import pytest
from django.urls import reverse

from bakery_app.product.models import FlavoursIceCream, MenuHeladeria, ProductosMenu  # , FlavourName,
from bakery_app.product.views import ProductCreate, ProductDelete, ProductUpdate


@pytest.mark.django_db
def test_Product_View_get_products(client, products_create):
    data = MenuHeladeria.objects.all()
    assert data.count() > 0
    response = client.get(reverse("product:product"))
    assert "Productos del Menu" in str(response.content)
    assert "Peso de la Bola de Helado" in str(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_products__logged(admin_user, rf, params_menu_products):
    request = rf.post(
        reverse("product:create"),
        data=params_menu_products,
    )
    assert MenuHeladeria.objects.count() == 0
    request.user = admin_user
    response = ProductCreate.as_view()(request)
    assert response.status_code == 204
    assert MenuHeladeria.objects.count() == 1


@pytest.mark.django_db
def test_create_products__NOT_logged(client, params_menu_products):
    request = client.post(
        reverse("product:create"),
        data=params_menu_products,
    )
    products_founded = MenuHeladeria.objects.all()
    assert request.status_code == 302
    assert request.url == "/admin/login/?next=/product/create/"
    assert products_founded.count() == 0


@pytest.mark.django_db
def test_create_products__invalid(admin_user, rf):
    request = rf.post(
        reverse("product:create"),
        data={
            "productos_menu": "",
            "precio": 1.50,
            "peso_en_helado": 200,
        },
    )
    products_founded = ProductosMenu.objects.all()
    request.user = admin_user
    response = ProductCreate.as_view()(request)
    assert response.status_code == 200
    assert products_founded.count() == 0


@pytest.mark.django_db
def test_update_products_views__access_logged_ussers(client, products_create, django_user_model):
    user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678")
    client.login(username=user.email, password="12345678")
    product = MenuHeladeria.objects.first()
    response = client.get(reverse("product:update", kwargs={"pk": product.pk}))
    assert response.status_code == 200
    assert "Editar el Producto al Menu" in str(response.content)


@pytest.mark.django_db
def test_update_products__update_data(admin_user, rf, one_product_create):
    product_update = MenuHeladeria.objects.first()
    num = product_update.pk
    print(product_update.pk, product_update.productos_menu.pk)
    request = rf.post(
        reverse("product:update", kwargs={"pk": num}),
        data={
            "productos_menu": product_update.productos_menu.pk,
            "precio": 1.05,
            "peso_en_helado": 200,
        },
    )
    request.user = admin_user
    response = ProductUpdate.as_view()(request, pk=num)
    product_update = MenuHeladeria.objects.first()
    assert response.status_code == 204
    assert MenuHeladeria.objects.count() == 1
    assert product_update.precio == Decimal("1.05")
    assert product_update.peso_en_helado == 200


@pytest.mark.django_db
def test_delete_products_views(client, admin_user, products_create, django_user_model):
    user = django_user_model.objects.create_user(email="Carlos@gmail.com", password="12345678", is_staff=True)
    client.login(username=user.email, password="12345678")
    product = MenuHeladeria.objects.first()
    response = client.get(reverse("product:delete", kwargs={"pk": product.pk}))
    assert response.status_code == 200
    assert "ELIMINAR PRODUCTO" in str(response.content)
    assert "Estas Seguro de eliminar" in str(response.content)


@pytest.mark.django_db
def test_delete_product(admin_user, rf, products_create):
    inicial_count = MenuHeladeria.objects.count()
    product = MenuHeladeria.objects.first()
    request = rf.post("product:delete", kwargs={"pk": product.pk})
    request.user = admin_user
    response = ProductDelete.as_view()(request, pk=product.pk)
    assert response.status_code == 204
    after_delete = MenuHeladeria.objects.count()
    assert inicial_count - 1 == after_delete


@pytest.mark.django_db
def test_Flavours_View_get_flavours(client, flavours_create):
    data = FlavoursIceCream.objects.all()
    assert data.count() > 0
    response = client.get(reverse("product:flavour"))
    assert response.status_code == 200
