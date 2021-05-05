from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import Fridge, Picture, Favorite, Manager, Notification, KmlFile
from django.contrib.auth.models import User
from .serializers import FridgeSerializer, PictureSerializer, FavoriteSerializer, ManagerSerializer, CustomTokenObtainPairSerializer, NotificationSerializer, KmlFileSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from .permissions import IsManagerOf, IsAdminUserOrReadOnly
from django.core.mail import mail_managers

class FridgeViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsManagerOf, )

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if (name):
            self.queryset = Fridge.objects.filter(name=name)
        return self.queryset

class PictureViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class FavoriteViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user = self.request.query_params.get('user')
        fridge = self.request.query_params.get('fridge')
        if (user):
            self.queryset = Favorite.objects.filter(user__id=user)
        if (fridge):
            self.queryset = Favorite.objects.filter(fridge__id=fridge)
        return self.queryset

    def create(self, request):
        new_favorite = Favorite()
        new_favorite.user = User.objects.filter(id=request.data['user'])[0]
        new_favorite.fridge = Fridge.objects.filter(id=request.data['fridge'])[0]
        new_favorite.save()
        return HttpResponse(new_favorite.id)

class ManagerViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = (IsAdminUserOrReadOnly, )

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if (user):
            self.queryset = Manager.objects.filter(user__id=user)
        return self.queryset

    def create(self, request):
        new_manager = Manager()
        new_manager.user = User.objects.filter(id=request.data['user'])[0]
        new_manager.fridge = Fridge.objects.filter(id=request.data['fridge'])[0]
        new_manager.save()
        return HttpResponse(new_manager.id)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user = self.request.query_params.get('user')
        fridge = self.request.query_params.get('fridge')
        if (user):
            self.queryset = Notification.objects.filter(user__id=user)
        if (fridge):
            self.queryset = Notification.objects.filter(fridge__id=fridge)
        return self.queryset

class KmlFileViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer,]
    queryset = KmlFile.objects.all()
    serializer_class = KmlFileSerializer
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def upload(self ,request):
        file_serializer = KmlFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

def send_email_view(request):
    subject = request.GET['subject']
    message = 'NE PAS RÉPONDRE À CE MAIL\nSi vous souhaitez contacter la personne ayant envoyé ce message, contactez-la à cette addresse: ' + request.GET['sender_email'] + '\n\n'
    message += 'Message:\n' + request.GET['message']

    mail_managers(subject, message)
    return HttpResponse('Email sent')