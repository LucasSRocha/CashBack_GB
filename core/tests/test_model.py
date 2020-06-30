import pytest
from rest_framework.exceptions import ValidationError

from core.models import PreApprovedSales, RegisteredSale
from core.serializers import (PreApprovedSalesSerializer,
                              RegisteredSaleSerializer)


@pytest.mark.django_db
def test_create_sale(registered_sale_payload, super_user, expected_percentage):
    serializer = RegisteredSaleSerializer(data=registered_sale_payload)
    serializer.is_valid()
    assert not RegisteredSale.objects.filter(user=super_user).exists()
    obj = serializer.create_sale(
        validated_data=serializer.validated_data, user=super_user
    )
    assert RegisteredSale.objects.filter(user=super_user).exists()
    assert obj.percentage_applied == expected_percentage


@pytest.mark.django_db
def test_create_pre_approved_sale(cpf_payload):
    serializer = PreApprovedSalesSerializer(data=cpf_payload)
    serializer.is_valid()
    serializer.save()
    assert PreApprovedSales.objects.filter(**cpf_payload).exists()


@pytest.mark.django_db
def test_create_invalid_pre_approved_sale(invalid_cpf_payload):
    with pytest.raises(ValidationError):
        serializer = PreApprovedSalesSerializer(data=invalid_cpf_payload)
        serializer.is_valid(raise_exception=True)
