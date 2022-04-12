from rest_framework.serializers import ModelSerializer

from track.models import Track, Card


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = (
            'article',
            'start_check',
            'end_check',
            'step',
        )
