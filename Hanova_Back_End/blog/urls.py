from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

# Router automatically creates all the URL patterns
router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]