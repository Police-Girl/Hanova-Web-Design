from django.shortcuts import render
from rest_framework import viewsets
from .models import Inquiry
from .serializers import InquirySerializer

# Handles all CRUD operations for Inquiry
# GET all, POST new, GET one, PUT update, DELETE
class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()  # fetch all inquiries from DB
    serializer_class = InquirySerializer  # use our serializer to convert to JSON

# Create your views here.
from rest_framework.permissions import IsAuthenticated

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]  # only logged in users can access