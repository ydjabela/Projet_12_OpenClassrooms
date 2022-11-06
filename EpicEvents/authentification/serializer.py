from rest_framework import serializers

# Local Libs
from .models import Client, User


class ClientSerializer(serializers.ModelSerializer):
    """
    Client serializer
    Based on serializers.ModelSerializer
    """
    class Meta:
        model = Client
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    Based on serializers.ModelSerializer
    """
    class Meta:
        model = User
        fields = "__all__"
