from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Fridge, Picture, Favorite, Manager, Notification
from django.contrib.auth.models import User

class PictureSerializer(serializers.ModelSerializer):
    fridge = serializers.StringRelatedField()
    image_url = serializers.SerializerMethodField

    class Meta:
        model = Picture
        fields = '__all__'

class FridgeSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True)
    menu_list = serializers.JSONField()

    class Meta:
        model = Fridge
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fridge = serializers.StringRelatedField()

    class Meta:
        model = Favorite
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fridge = serializers.PrimaryKeyRelatedField(queryset=Fridge.objects.all())
    fridge_name = serializers.StringRelatedField(source='fridge', read_only=True)

    class Meta:
        model = Manager
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data
        data.update({'userId': self.user.id})
        return data

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fridge = serializers.PrimaryKeyRelatedField(queryset=Fridge.objects.all())
    fridge_name = serializers.StringRelatedField(source='fridge', read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'