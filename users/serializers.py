from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     about_me = serializers.CharField(source='profile.about_me')
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'about_me']
        
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    
    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "id",]

