import pytest
from rest_framework.exceptions import ValidationError

from users.models import User
from users.serializers import UserSerializer


@pytest.mark.django_db
def test_create_user(user_payload):
    serializer = UserSerializer(data=user_payload)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    assert User.objects.filter(email=user_payload["email"]).exists()


@pytest.mark.django_db
def test_create_invalid_cpf_user(user_invalid_cpf_payload):
    with pytest.raises(ValidationError):
        serializer = UserSerializer(data=user_invalid_cpf_payload)
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_create_invalid_email_user(user_invalid_email_payload):
    with pytest.raises(ValidationError):
        serializer = UserSerializer(data=user_invalid_email_payload)
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_create_invalid_password_user(user_invalid_password_payload):
    with pytest.raises(ValidationError):
        serializer = UserSerializer(data=user_invalid_password_payload)
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_create_invalid_full_name_user(user_invalid_full_name_payload):
    with pytest.raises(ValidationError):
        serializer = UserSerializer(data=user_invalid_full_name_payload)
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_user_repr(custom_user):
    assert str(custom_user) == custom_user.email
