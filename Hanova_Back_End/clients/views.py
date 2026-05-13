from django.shortcuts import render
from rest_framework import viewsets
from .models import clients
from .serializers import ClientSerializers

#Crud operations for clients
#get all, post new, get one, update, delete
class clientsViewSet(viewsets.ModelViewSet):
    queryset = clients.objects.all()  #fetch all clients from DB
    serializer_class = ClientSerializers  #use our serializer to convert to JSON
# Create your views here.
from rest_framework.permissions import IsAuthenticated

class clientsViewSet(viewsets.ModelViewSet):
    queryset = clients.objects.all()
    serializer_class = ClientSerializers
    permission_classes = [IsAuthenticated]  # only logged in users can access
