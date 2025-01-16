from rest_framework import serializers
from .models import Account, Destination, Incoming

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'account_name', 'website']

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['account_id', 'url', 'http_method', 'headers']

class IncomingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incoming
        fields = ['destination_id', 'data']
