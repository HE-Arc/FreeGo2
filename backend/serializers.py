from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Fridge, Picture, Favorite, Manager, Notification, KmlFile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.files import File

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

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
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

class KmlFileSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    geojson_file = serializers.SerializerMethodField()

    class Meta:
        model = KmlFile
        fields = '__all__'

    def get_geojson_file(self, obj):
        f = open(obj.geojson_file.path, 'rb')
        geojson = File(f)
        data = geojson.read()
        f.close()
        return data

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password1": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password1'])
        user.save()

        return user