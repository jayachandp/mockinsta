from rest_framework import serializers
from .models import User, InstaPost


class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField(source='get_followers_count')
    following_count = serializers.SerializerMethodField(source='get_following_count')

    def get_followers_count(self, obj):
        return obj.follower.all().count()

    def get_following_count(self, obj):
        return obj.following.all().count()

    class Meta:
        model = User
        fields = ['username', 'email', 'followers_count', 'following_count']


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class InstaPostSerializer(serializers.ModelSerializer):
    likes = BaseUserSerializer(many=True)
    likes_count = serializers.SerializerMethodField(source='get_likes_count')

    def get_likes_count(self, obj):
        return obj.no_of_likes

    class Meta:
        model = InstaPost
        fields = "__all__"