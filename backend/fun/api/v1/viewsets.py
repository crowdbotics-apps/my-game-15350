from rest_framework import authentication
from fun.models import Battle
from .serializers import BattleSerializer
from rest_framework import viewsets


class BattleViewSet(viewsets.ModelViewSet):
    serializer_class = BattleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Battle.objects.all()
