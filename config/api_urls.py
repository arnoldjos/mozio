from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mozio.providers.api import viewsets as provider_viewsets

router = DefaultRouter()
router.register(r"providers", provider_viewsets.ProviderViewSet)
router.register(r"service_areas", provider_viewsets.ServiceAreaViewSet)

api_urlpatterns = [
    path("mozio_api/", include(router.urls))
]