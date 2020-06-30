from django.contrib import admin

from .models import PreApprovedSales, RegisteredSale

admin.site.register(PreApprovedSales)
admin.site.register(RegisteredSale)
