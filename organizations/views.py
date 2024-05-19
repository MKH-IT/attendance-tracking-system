from rest_framework import viewsets

from .models import Organizations
from .serializers import OrganizationsSerializer


class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all().order_by('id')
    serializer_class = OrganizationsSerializer
    schema_tags = ["organizations"]
