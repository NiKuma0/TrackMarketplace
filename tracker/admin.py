from django.contrib import admin

from tracker.models import Tracker, Card


@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_fields = (
        'article',
        'user',
    )

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
