from django.contrib import admin

from tracker.models import Tracker


@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_fields = (
        'article',
        'user',
    )
