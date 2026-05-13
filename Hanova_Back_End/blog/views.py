from django.shortcuts import render
from rest_framework import viewsets
from .models import blog_posts
from .serializers import BlogPostSerializer

#handles all CRUD operations for BlogPost
#gets all, posts new, gets one, updates, deletes
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = blog_posts.objects.all()  #fetch all blog posts from DB
    serializer_class = BlogPostSerializer  #use our serializer to convert to JSON

# Create your views here.
from rest_framework.permissions import IsAuthenticated

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = blog_posts.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]  # only logged in users can access
