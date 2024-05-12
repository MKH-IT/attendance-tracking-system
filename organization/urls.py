from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet

router = DefaultRouter()
router.register(r'', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
