from django_filters import rest_framework as filters

from ..models import ServiceArea


class ServiceAreaFilter(filters.FilterSet):
    class Meta:
        model = ServiceArea
        fields = "__all__"
