from rest_framework import serializers
from .models import Fridge, Picture

class FridgeSerializer(serializers.ModelSerializer):
    pictures = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, read_only=True)
    
    class Meta:
        model = Fridge
        fields = '__all__'

class PictureSerializer(serializers.ModelSerializer):
    fridge = serializers.StringRelatedField()

    class Meta:
        model = Picture
        fields = '__all__'