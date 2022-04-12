from rest_framework import serializers

from tracker.models import Tracker, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = (
            'article',
            'start_check',
            'end_check',
            'step',
        )

class RetriveTrackerSerializer(serializers.ModelSerializer):
    histrory = CardSerializer(many=True)

    class Meta:
        model = Tracker
        fields = (
            'article',
            'start_check',
            'end_check',
            'step',
            'history',
        )
