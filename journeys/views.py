from rest_framework import viewsets

from .models import Journey
from .serializers import JourneySerializer


class JourneyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    lookup_field = 'slug'
