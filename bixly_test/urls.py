from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('', include('transport.urls')),
]
