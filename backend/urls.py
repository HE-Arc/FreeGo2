from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import MyTokenObtainPairView

urlpatterns = [
    path('api-token/', MyTokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]