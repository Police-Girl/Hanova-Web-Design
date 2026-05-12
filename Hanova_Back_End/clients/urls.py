from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import clientsViewSet

# Router automatically creates all the URL patterns for us
router = DefaultRouter()
router.register(r'clients', clientsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]