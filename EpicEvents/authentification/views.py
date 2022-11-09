from django.shortcuts import render
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


class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    # permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]

    def list(self, request):
        clients = Client.objects.all()
        if clients is not None:
            serialized_clients = ClientSerializer(clients, many=True)
            return response.Response(data=serialized_clients.data, status=status.HTTP_200_OK)
        else:
            return response.Response(
                data={"detail": "No client available."},
                status=status.HTTP_204_NO_CONTENT
            )

    def retrieve(self, request, pk):
        try:
            client = Client.objects.get(id=pk)
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

    def create(self, request):
        try:
            content = dict(request.data.items())
        except Exception:
            return response.Response(
                data={"detail": "Form is invalid."},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        try:
            client_update = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
