from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/', include('track.urls')),
    path('api/v1/', include('user.urls'))
)
