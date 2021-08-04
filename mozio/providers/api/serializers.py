from rest_framework import serializers

from ..models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    provider_data = serializers.SerializerMethodField()

    class Meta:
        model = ServiceArea
        fields = "__all__"

    def get_provider_data(self, obj):
        return ProviderSerializer(obj.provider, many=False, read_only=True,
                                  context={"request": self.context.get("request")}).data
