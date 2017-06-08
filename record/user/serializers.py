from rest_framework import serializers

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
