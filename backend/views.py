from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import Fridge, Picture, Favorite
from .serializers import FridgeSerializer, PictureSerializer, FavoriteSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

class FridgeViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Fridge.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = FridgeSerializer

class PictureViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        fridge = self.request.query_params.get('fridge')
        queryset = Favorite.objects.filter(user__id=user).filter(fridge__id=fridge)
        return queryset

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer