from rest_framework.routers import DefaultRouter
from .views import OrganizationsViewSet

router = DefaultRouter()
router.register(r'', OrganizationsViewSet, basename='organizations')

urlpatterns = []
urlpatterns += router.urls
