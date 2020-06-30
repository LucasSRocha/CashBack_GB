import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_create_user_view(client, user_payload):
    url = reverse("users:viewset-list")
    response = client.post(url, user_payload)
    assert response.status_code == 201
    assert User.objects.filter(email=user_payload["email"]).exists()


@pytest.mark.django_db
def test_unauthorized_get_user_view(client, custom_user):
    url = f'{reverse("users:viewset-list")}{custom_user.pk}/'
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_user_view(client, custom_user, password):
    url = f'{reverse("users:viewset-list")}{custom_user.pk}/'
    auth_url = reverse("users:auth")
    response = client.post(auth_url, {"email": custom_user.email, "password": password})
    assert response.status_code == 200

    token = f"Bearer {response.json()['access']}"
    response = client.get(url, HTTP_AUTHORIZATION=token)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_get_another_user_view(
    client, custom_user, password, custom_user_2
):
    url = f'{reverse("users:viewset-list")}{custom_user_2.pk}/'
    auth_url = reverse("users:auth")
    response = client.post(auth_url, {"email": custom_user.email, "password": password})
    assert response.status_code == 200

    token = f"Bearer {response.json()['access']}"
    response = client.get(url, HTTP_AUTHORIZATION=token)
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_permission(custom_user, client_admin):
    url = f'{reverse("users:viewset-list")}{custom_user.pk}/'
    response = client_admin.get(url)
    assert response.status_code == 200
