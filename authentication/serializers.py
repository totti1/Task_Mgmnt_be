from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "password",

        ]
        def create(self, validated_data):
            
            extra_kwargs = {"password": {"write_only": True}}
            password = self.validated_data["password"]
            account.make_password(password)
            # account.save()
            return account

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]