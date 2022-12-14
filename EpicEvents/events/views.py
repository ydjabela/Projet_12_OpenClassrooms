from rest_framework import (
    viewsets,
    status,
    response,
    permissions
)
from .models import Event
from authentification.models import Client
from contrat.models import Contrat
from .serializer import EventSerializer
from .permissions import EventPermissions
import logging
logger = logging.getLogger("EpicEvents")


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermissions]

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
        try:
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except (Contrat.DoesNotExist, ValueError):
            logger.warning("Contrat doesn't exist.")
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        event = Event.objects.filter(client=client, contrat=contrat)
        if event is not None:
            serialized_event = EventSerializer(event, many=True)
            return response.Response(data=serialized_event.data, status=status.HTTP_200_OK)
        else:
            logger.warning("No events available")
            return response.Response(
                data={"detail": "No event available."},
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
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except (Contrat.DoesNotExist, ValueError):
            logger.warning("Contract doesn't exist.")
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            event_id = int(request.resolver_match.kwargs["pk"])
            event = Event.objects.filter(id=event_id, client=client, contrat=contrat)
        except (Event.DoesNotExist, ValueError):
            logger.warning("Event doesn't exist.")
            return response.Response(
                data={"detail": "Event doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        if event is not None:
            serialized_event = EventSerializer(event, many=True)
            return response.Response(data=serialized_event.data, status=status.HTTP_200_OK)
        else:
            logger.warning("No event available.")
            return response.Response(
                data={"detail": "No event available."},
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
        try:
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except (Contrat.DoesNotExist, ValueError):
            logger.warning("Contract doesn't exist.")
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            support_contact = int(request.data["support_contact"])
        except ValueError:
            logger.warning("support contact doesn't exist.")
            content = {"detail": "support contact doesn't exist."}
            return response.Response(
                data=content,
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EventSerializer(
            data={
                "client": client.id,
                "contrat": contrat.id,
                "attendees": request.data["attendees"],
                "event_date": request.data["event_date"],
                "event_status": request.data["event_status"],
                "notes": request.data["notes"],
                "support_contact": support_contact,
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
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except (Contrat.DoesNotExist, ValueError):
            logger.warning("Contract doesn't exist.")
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            support_contact = int(request.data["support_contact"])
        except ValueError:
            logger.warning("support contact doesn't exist.")
            content = {"detail": "support contact doesn't exist."}
            return response.Response(
                data=content,
                status=status.HTTP_404_NOT_FOUND
            )
        data = {
                "client": client_id,
                "contrat": contrat_id,
                "attendees": request.data["attendees"],
                "event_date": request.data["event_date"],
                "event_status": request.data["event_status"],
                "notes": request.data["notes"],
                "support_contact": support_contact
            }

        try:
            event_id = int(request.resolver_match.kwargs["pk"])
            partial = kwargs.pop('partial', False)
            instance = Event.objects.get(id=event_id, client=client, contrat=contrat)
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return response.Response(serializer.data)
        except (Exception, ValueError):
            logger.warning("Event doesn't exist.")
            content = {"detail": "Event doesn't exist."}
            return response.Response(
                data=content,
                status=status.HTTP_404_NOT_FOUND
            )
