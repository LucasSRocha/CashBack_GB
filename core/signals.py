from decimal import Decimal

from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import RegisteredSale


def get_cashback_percentage_from_query(query: QuerySet, total: int = 0) -> Decimal:
    for i in query:
        total += i.value
    if total > 1500:
        return Decimal("0.20")
    elif 1000 < total <= 1500:
        return Decimal("0.15")
    else:
        return Decimal("0.10")


def update_query_with_new_cashback(query: QuerySet, new_percentage: Decimal) -> None:
    for i in query:
        i.cashback_amount = i.value * new_percentage
        i.percentage_applied = new_percentage
        i.save()


@receiver(post_save, sender=RegisteredSale)
def calculate_cashback(sender, instance, **kwargs):
    query = RegisteredSale.objects.filter(
        user=instance.user,
        date__month=instance.date.month,
        date__year=instance.date.year,
    )

    if query.exists():
        cashback_percentege = get_cashback_percentage_from_query(query=query)
        query = query.exclude(percentage_applied=cashback_percentege)
        update_query_with_new_cashback(query=query, new_percentage=cashback_percentege)
