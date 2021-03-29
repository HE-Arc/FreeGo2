from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Fridge, Picture, Favorite

class PictureSerializer(serializers.ModelSerializer):
    fridge = serializers.StringRelatedField()
    image_url = serializers.SerializerMethodField

    class Meta:
        model = Picture
        fields = '__all__'

class FridgeSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True)

    class Meta:
        model = Fridge
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    fridge = serializers.StringRelatedField()

    class Meta:
        model = Favorite
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data
        data.update({'userId': self.user.id})
        return data