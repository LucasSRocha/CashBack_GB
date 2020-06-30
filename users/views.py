from rest_framework import mixins, viewsets

from .models import User
from .permissions import AnonCreateUser, IsAdminOrSelf
from .serializers import UserSerializer


class UserViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf, AnonCreateUser]
