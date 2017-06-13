from rest_framework import serializers

from utils import customexception
from .models import User


class NormalUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, allow_blank=True)
    access_token = serializers.CharField(allow_blank=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'user_type',
            'access_token',
            'nickname',
        )

        extra_kwargs = {
            'password': {'write_only': True},
            'access_token': {'write_only': True},
            'user_type': {'write_only': True}
        }

    def create(self, validated_data):
        if 'password' in validated_data.keys():
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()

        else:
            raise customexception.ValidationException('Normal user required Password')

        return user
