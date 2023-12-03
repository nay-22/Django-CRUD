# artists/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Artist, Work

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'user', 'works']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type']

class WorkSerializerNew(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link', 'work_type']

