from rest_framework import serializers
from .models import blog_posts

# Converts BlogPost model into JSON for the frontend
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_posts
        fields = '__all__'  # expose all fields