from rest_framework.response import Response
from rest_framework import generics
from .models import Fridge, Picture, Favorite
from .serializers import FridgeSerializer, PictureSerializer, FavoriteSerializer
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