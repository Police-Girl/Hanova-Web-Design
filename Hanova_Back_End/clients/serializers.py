from rest_framework import serializers
from .models import clients

# Converts Client model into JSON for the frontend
class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = '__all__'  # expose all fields