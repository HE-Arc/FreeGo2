from rest_framework.response import Response
from rest_framework import generics
from .models import Fridge
from .serializers import FridgeSerializer

class FridgeView(generics.RetrieveAPIView):
    queryset = Fridge.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FridgeSerializer(queryset, many=True)
        return Response(serializer.data)