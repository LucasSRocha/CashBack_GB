import requests
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import PreApprovedSales, RegisteredSale
from .permissions import IsAdminOrOwner
from .serializers import PreApprovedSalesSerializer, RegisteredSaleSerializer


class PreApprovedSalesViewSet(viewsets.ModelViewSet):
    queryset = PreApprovedSales.objects.all()
    serializer_class = PreApprovedSalesSerializer
    permission_classes = [IsAdminUser]


class RegisteredSaleViewSet(viewsets.ModelViewSet):
    queryset = RegisteredSale.objects.all()
    serializer_class = RegisteredSaleSerializer
    permission_classes = [IsAdminOrOwner]

    def perform_create(self, serializer):
        serializer.create_sale(
            serializer.validated_data, serializer.context.get("request").user
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def total(self, request, *args, **kwargs):
        url = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={}".format(
            request.user.cpf
        )
        headers = {"token": settings.TOTAL_EXTERNAL_API_TOKEN}
        response = requests.get(url=url, headers=headers)
        result = response.json()

        if result.get("statusCode", 0) == 200 and (body := result.get("body", {})):
            return Response({"total": body.get("credit", 0)})
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
