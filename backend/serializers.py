from rest_framework import serializers
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