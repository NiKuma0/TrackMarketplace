from rest_framework import routers

from track.views import TracksViewsSet


track_router = routers.SimpleRouter()
track_router.register(r'tracks', TracksViewsSet)

urlpatterns = track_router.urls
