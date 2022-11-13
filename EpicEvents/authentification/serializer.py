from rest_framework import serializers
from django.contrib.auth.hashers import make_password

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

    date_joined = serializers.ReadOnlyField()

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password', "role", "phone_number")
        extra_kwargs = {'password': {'write_only': True}}
