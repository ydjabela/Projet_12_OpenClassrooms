from rest_framework import (
    viewsets,
    status,
    response,
    permissions
)
from .models import Contrat
from authentification.models import Client
from .serializer import ContratSerializer
from .permissions import ContratPermissions
import logging
logger = logging.getLogger("EpicEvents")


class ContratView(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    permission_classes = [permissions.IsAuthenticated, ContratPermissions]

    def list(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except (Client.DoesNotExist, ValueError):
            logger.warning("Client doesn't exist.")
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        contrat = Contrat.objects.filter(client=client)
        if contrat is not None:
            serialized_contrat = ContratSerializer(contrat, many=True)
            return response.Response(data=serialized_contrat.data, status=status.HTTP_200_OK)
        else:
            logger.warning("No contrat available.")
            return response.Response(
                data={"detail": "No contrat available."},
                status=status.HTTP_204_NO_CONTENT
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except (Client.DoesNotExist, ValueError):
            logger.warning("Client doesn't exist.")
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            contrat_id = int(request.resolver_match.kwargs["pk"])
            contrat = Contrat.objects.filter(id=contrat_id, client=client)
        except (Contrat.DoesNotExist, ValueError):
            logger.warning("Contrat doesn't exist.")
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        if contrat is not None:
            serialized_contrat = ContratSerializer(contrat, many=True)
            return response.Response(data=serialized_contrat.data, status=status.HTTP_200_OK)
        else:
            logger.warning("No contrat available.")
            return response.Response(
                data={"detail": "No contrat available."},
                status=status.HTTP_204_NO_CONTENT
            )

    def create(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except (Client.DoesNotExist, ValueError):
            logger.warning("Client doesn't exist.")
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ContratSerializer(
            data={
                "client": client.id,
                "status": request.data["status"],
                "amount": request.data["amount"],
                "payment_due": request.data["payment_due"],
                "sales_contact": request.data["sales_contact"],  # TODO automatique user
            })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except (Client.DoesNotExist, ValueError):
            logger.warning("Client doesn't exist.")
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            sales_contact = int(request.data["sales_contact"])
        except ValueError:
            logger.warning("Sales contact doesn't exist.")
            content = {"detail": "Sales contact doesn't exist."}
            return response.Response(
                data=content,
                status=status.HTTP_404_NOT_FOUND
            )

        data = {
            "client": client_id,
            "status": request.data["status"],
            "amount": request.data["amount"],
            "payment_due": request.data["payment_due"],
            "sales_contact": sales_contact,
        }
        try:
            contrat_id = int(request.resolver_match.kwargs["pk"])
            partial = kwargs.pop('partial', False)
            instance = Contrat.objects.get(id=contrat_id, client=client)
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return response.Response(serializer.data)
        except (Exception, ValueError):
            logger.warning("contrat doesn't exist.")
            content = {"detail": "contrat doesn't exist."}
            return response.Response(
                data=content,
                status=status.HTTP_404_NOT_FOUND
            )
