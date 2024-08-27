import pytest

from bakery_app.product.tests.factories import ProductFactory
from bakery_app.users.models import User
from bakery_app.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def user_factory():
    def factory(**kwargs):
        return UserFactory(**kwargs)

    return factory


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return ProductFactory(**kwargs)

    return factory
