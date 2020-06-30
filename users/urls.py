from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register("", UserViewSet, basename="viewset")

urlpatterns = [
    path("auth/", TokenObtainPairView.as_view(), name="auth"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth_refresh"),
    path("", include(router.urls),),
]
