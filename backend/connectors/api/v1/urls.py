from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135618ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135618", Testconnectors135618ViewSet, basename="testconnectors135618"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
