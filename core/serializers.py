from decimal import Decimal
from typing import Tuple

from rest_framework import serializers

from users.serializers import UserSerializer

from .models import PreApprovedSales, RegisteredSale


class RegisteredSaleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cashback_amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )
    percentage_applied = serializers.DecimalField(
        max_digits=4, decimal_places=2, read_only=True
    )
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = RegisteredSale
        fields = [
            "user",
            "code",
            "value",
            "date",
            "cashback_amount",
            "percentage_applied",
            "status",
        ]

    def create_sale(self, validated_data, user):
        cashback_amount, percentage_applied = self.apply_cashback(
            validated_data.get("value", 0)
        )
        if PreApprovedSales.objects.filter(cpf=user.cpf).exists():
            validated_data["status"] = self.Meta.model.APPROVED
        validated_data["cashback_amount"] = cashback_amount
        validated_data["percentage_applied"] = percentage_applied

        obj = self.save(user=user)
        return obj

    @staticmethod
    def apply_cashback(value: Decimal) -> Tuple[Decimal, Decimal]:
        if not isinstance(value, Decimal):
            value = Decimal(value)
        if value > 1500:
            percentage = Decimal("0.20")
        elif 1000 < value <= 1500:
            percentage = Decimal("0.15")
        else:
            percentage = Decimal("0.10")

        cashback = value * percentage
        return cashback, percentage


class PreApprovedSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreApprovedSales
        fields = "__all__"
