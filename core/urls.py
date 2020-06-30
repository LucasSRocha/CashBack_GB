from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PreApprovedSalesViewSet, RegisteredSaleViewSet

app_name = "core"

router = DefaultRouter()
router.register("preapproved", PreApprovedSalesViewSet)
router.register("sale", RegisteredSaleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
