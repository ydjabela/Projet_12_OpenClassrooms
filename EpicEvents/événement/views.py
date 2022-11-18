from django.shortcuts import render
from rest_framework import (
    viewsets,
    generics,
    status,
    renderers,
    response,
    permissions
)
from .models import Event
from authentification.models import Client
from contrat.models import Contrat
from .serializer import EventSerializer
from .permissions import EventPermissions


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermissions]

    def list(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except Contrat.DoesNotExist:
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        event = Event.objects.filter(client=client, contrat=contrat)
        if event is not None:
            serialized_event = EventSerializer(event, many=True)
            return response.Response(data=serialized_event.data, status=status.HTTP_200_OK)
        else:
            return response.Response(
                data={"detail": "No event available."},
                status=status.HTTP_204_NO_CONTENT
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except Contrat.DoesNotExist:
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        event_id = int(request.resolver_match.kwargs["pk"])
        event = Event.objects.filter(id=event_id, client=client, contrat=contrat)
        if event is not None:
            serialized_event = EventSerializer(event, many=True)
            return response.Response(data=serialized_event.data, status=status.HTTP_200_OK)
        else:
            return response.Response(
                data={"detail": "No event available."},
                status=status.HTTP_204_NO_CONTENT
            )

    def create(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except Contrat.DoesNotExist:
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EventSerializer(
            data={
                "client": client_id,
                "contrat": contrat_id,
                "attendees": request.data["attendees"],
                "event_date": request.data["event_date"],
                "event_status": request.data["event_status"],
                "notes": request.data["notes"],
                "support_contact": request.data["support_contact"],  # TODO automatique user
            })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        try:
            client_id = kwargs["client_id"]
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return response.Response(
                data={"detail": "Client doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            contrat_id = kwargs["contrat_id"]
            contrat = Contrat.objects.get(id=contrat_id)
        except Contrat.DoesNotExist:
            return response.Response(
                data={"detail": "Contrat doesn't exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        data = {
                "client": client_id,
                "contrat": contrat_id,
                "attendees": request.data["attendees"],
                "event_date": request.data["event_date"],
                "event_status": request.data["event_status"],
                "notes": request.data["notes"],
                "support_contact": request.data["support_contact"],  # TODO automatique user
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
        except Exception:
            content = {"detail": "Event doesn't exist."}
            return response.Response(
                data=content,
                status=status.HTTP_404_NOT_FOUND
            )
