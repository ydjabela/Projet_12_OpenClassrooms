from rest_framework import serializers
from .models import Contrat


class ContratSerializer(serializers.ModelSerializer):
    """
    Contrat serializer
    Based on serializers.ModelSerializer
    """
    class Meta():
        model = Contrat
        fields = "__all__"
