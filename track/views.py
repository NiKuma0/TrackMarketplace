from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from track.serializers import CardSerializer, TrackSerializer
from track.models import Card, Track


class CardsViewSet(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    paginator = None


class TracksViewsSet(ModelViewSet):
    serializer_class = TrackSerializer
    permissions = (IsAuthenticated,)
    queryset = Track.objects.all()

    @action(('GET',), detail=False)
    def my_tracks(self, request, *args, **kwargs):
        """Возвращает трекеры пользавателя"""
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
