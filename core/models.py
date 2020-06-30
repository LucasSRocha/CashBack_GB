from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.db import models
from localflavor.br.models import BRCPFField

from utils import clean_string_punctuation

User = get_user_model()


class RegisteredSale(models.Model):
    IN_VALIDATION = 0
    APPROVED = 1
    STATUS_CHOICES = (
        (IN_VALIDATION, "Em validação"),
        (APPROVED, "Aprovado"),
    )

    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    code = models.CharField(max_length=255)
    value = models.DecimalField(
        max_digits=20, decimal_places=2, blank=False, null=False
    )
    date = models.DateField(blank=False, null=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    cashback_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    percentage_applied = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.cpf} - R${self.value}"

    class Meta:
        ordering = [
            "date",
        ]


class PreApprovedSalesManager(BaseUserManager):
    def create(
        self, cpf: str,
    ):
        if not cpf:
            raise ValueError("CPF required")

        obj = self.model(cpf=clean_string_punctuation(cpf))
        obj.save()
        return obj


class PreApprovedSales(models.Model):
    cpf = BRCPFField(unique=True)
    objects = PreApprovedSalesManager()

    def __str__(self):
        return f"{self.cpf}"
