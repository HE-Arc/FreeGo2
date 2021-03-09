from rest_framework.response import Response
from rest_framework import generics
from .models import Fridge, Picture
from .serializers import FridgeSerializer, PictureSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .custom_renderers import JPEGRenderer, PNGRenderer

class FridgeViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer

class PictureViewSet(viewsets.ModelViewSet):
    renderer_classes = [JPEGRenderer, PNGRenderer]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

""" class FridgeView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Fridge.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FridgeSerializer(queryset, many=True)
        return Response(serializer.data) """