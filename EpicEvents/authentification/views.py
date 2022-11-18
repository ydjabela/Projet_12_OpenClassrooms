from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import (
    viewsets,
    generics,
    status,
    renderers,
    response,
    permissions
)
from .models import Client, User
from .serializer import ClientSerializer, UserSerializer
from .permissions import ClientPermissions, UserPermissions


class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermissions]

    def list(self, request, *args, **kwargs):
        clients = Client.objects.all()
        if clients is not None:
            serialized_clients = ClientSerializer(clients, many=True)
            return response.Response(data=serialized_clients.data, status=status.HTTP_200_OK)
        else:
            return response.Response(
                data={"detail": "No client available."},
                status=status.HTTP_204_NO_CONTENT
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            client_id = int(request.resolver_match.kwargs["pk"])
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serialized_client = ClientSerializer(client)
        if serialized_client.data:
            content = serialized_client.data
            return response.Response(
                data=content,
                status=status.HTTP_200_OK
            )
        else:
            return response.Response(
                data={"detail": "Client details not available."},
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request, *args, **kwargs):
        user = request.data
        serializer = ClientSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        phone = request.data["phone"]
        mobile = request.data["mobile"]
        company_name = request.data["company_name"]
        sales_contact = request.data["sales_contact"]
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "mobile": mobile,
            "company_name": company_name,
            "sales_contact": sales_contact,
        }
        try:
            client_id = int(request.resolver_match.kwargs["pk"])
            partial = kwargs.pop('partial', False)
            instance = Client.objects.get(id=client_id)
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return response.Response(serializer.data)
        except Exception:
            content = {"detail": "Client doesn't exist."}
            return response.Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (permissions.IsAuthenticated, UserPermissions)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
