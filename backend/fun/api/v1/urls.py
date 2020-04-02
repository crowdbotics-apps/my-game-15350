from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BattleViewSet

router = DefaultRouter()
router.register("battle", BattleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
