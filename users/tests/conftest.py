import pytest

from users.models import User


@pytest.fixture
def full_name():
    return "Lucas Rocha"


@pytest.fixture
def invalid_full_name():
    return ""


@pytest.fixture
def email():
    return "8rocha.lucas@gmail.com"


@pytest.fixture
def invalid_email():
    return "8..rocha.@lucas@gmail.com"


@pytest.fixture
def password():
    return "12345678"


@pytest.fixture
def invalid_password():
    return "1234"


@pytest.fixture
def cpf():
    return "123.456.789-09"


@pytest.fixture
def invalid_cpf():
    return "111.111.111-11"


@pytest.fixture
def user_payload(email, cpf, password, full_name):
    return {
        "cpf": cpf,
        "email": email,
        "password": password,
        "full_name": full_name,
    }


@pytest.fixture
def user_invalid_email_payload(invalid_email, cpf, password, full_name):
    return {
        "cpf": cpf,
        "email": invalid_email,
        "password": password,
        "full_name": full_name,
    }


@pytest.fixture
def user_invalid_cpf_payload(email, invalid_cpf, password, full_name):
    return {
        "cpf": invalid_cpf,
        "email": email,
        "password": password,
        "full_name": full_name,
    }


@pytest.fixture
def user_invalid_password_payload(email, cpf, invalid_password, full_name):
    return {
        "cpf": invalid_cpf,
        "email": email,
        "password": password,
        "full_name": full_name,
    }


@pytest.fixture
def user_invalid_full_name_payload(email, cpf, password, invalid_full_name):
    return {
        "cpf": cpf,
        "email": email,
        "password": password,
        "full_name": invalid_full_name,
    }


@pytest.fixture
def custom_user(user_payload):
    return User.objects.create(**user_payload)


@pytest.fixture
def custom_user_2(password, full_name):
    return User.objects.create(
        **{
            "cpf": "36270582830",
            "email": "email@email.com",
            "password": password,
            "full_name": full_name,
        }
    )
