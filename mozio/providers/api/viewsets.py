from rest_framework import viewsets

from .serializers import ProviderSerializer, ServiceAreaSerializer
from ..models import Provider, ServiceArea
from .filters import ServiceAreaFilter


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.select_related("provider").all()
    serializer_class = ServiceAreaSerializer
    filterset_class = ServiceAreaFilter

    def get_serializer_context(self):
        context = super(ServiceAreaViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
