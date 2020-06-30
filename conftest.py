import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def admin_password():
    return "admin"


@pytest.fixture
def admin_email():
    return "admin@admin.com"


@pytest.fixture
def admin_cpf():
    return "15350946056"


@pytest.fixture
def super_user(django_user_model, admin_password, admin_email, admin_cpf):
    return django_user_model.objects.create(
        **{
            "email": admin_email,
            "password": admin_password,
            "full_name": "admin",
            "cpf": admin_cpf,
            "is_staff": True,
            "is_active": True,
            "is_superuser": True,
        }
    )


@pytest.fixture
def client_admin(super_user, admin_email, admin_password):
    token = RefreshToken.for_user(super_user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
    return client
