from datetime import date
from decimal import Decimal

import pytest

from core.models import PreApprovedSales, RegisteredSale
from core.serializers import (PreApprovedSalesSerializer,
                              RegisteredSaleSerializer)


@pytest.fixture
def cpf():
    return "12345678909"


@pytest.fixture
def invalid_cpf():
    return "cpfinvalido"


@pytest.fixture
def cpf_payload(cpf):
    return {"cpf": cpf}


@pytest.fixture
def invalid_cpf_payload(invalid_cpf):
    return {"cpf": invalid_cpf}


@pytest.fixture
def pre_approved_cpf(cpf_payload):
    return PreApprovedSales.objects.create(**cpf_payload)


@pytest.fixture
def admin_pre_approved_cpf(admin_cpf):
    return PreApprovedSales.objects.create(cpf=admin_cpf)


@pytest.fixture
def sale_code():
    return "1223334444"


@pytest.fixture
def sale_value():
    return Decimal("1000.00")


@pytest.fixture
def expected_percentage():
    return Decimal("0.10")


@pytest.fixture
def sale_date():
    return date.today()


@pytest.fixture
def registered_sale_payload(sale_code, sale_value, sale_date):
    return {
        "code": sale_code,
        "value": sale_value,
        "date": sale_date,
    }


@pytest.fixture
def registered_sale(registered_sale_payload):
    return RegisteredSale.objects.create(**registered_sale_payload)
