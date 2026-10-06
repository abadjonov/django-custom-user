from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        model = User
