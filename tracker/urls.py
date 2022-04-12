from rest_framework import routers

from tracker.views import TrackersViewsSet


tracker_router = routers.SimpleRouter()
tracker_router.register(r'trackers', TrackersViewsSet)

urlpatterns = tracker_router.urls
