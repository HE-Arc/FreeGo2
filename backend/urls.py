from django.urls import path, include
from rest_framework import routers
from backend import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import MyTokenObtainPairView

router = routers.DefaultRouter()
router.register(r'fridge', views.FridgeViewSet)
router.register(r'picture', views.PictureViewSet)
router.register(r'favorite', views.FavoriteViewSet)

urlpatterns = [
    path('api-token/', MyTokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]