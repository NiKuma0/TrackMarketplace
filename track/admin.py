from django.contrib import admin

from track.models import Track


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_fields = (
        'article',
        'user',
    )
