from django.urls import path, include
from rest_framework import routers, permissions
from backend import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import MyTokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'fridge', views.FridgeViewSet)
router.register(r'picture', views.PictureViewSet)
router.register(r'favorite', views.FavoriteViewSet)
router.register(r'manager', views.ManagerViewSet)
router.register(r'notification', views.NotificationViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Free Go API",
      default_version='v1',
      description="API for Free Go's application",
      #terms_of_service="https://www.freego.com/policies/terms/",
      #contact=openapi.Contact(email="contact@freego.local"),
      #license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api-token/', MyTokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]