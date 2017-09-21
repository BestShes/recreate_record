from django.contrib.auth import authenticate
from rest_auth.app_settings import create_token
from rest_auth.models import TokenModel
from rest_framework import serializers

from utils import customexception, sendemail
from .models import Member


class NormalUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, allow_blank=True)
    access_token = serializers.CharField(allow_blank=True)

    class Meta:
        model = Member
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
            user = Member(**validated_data)
            user.set_password(password)
            user.is_active = False
            user.save()
            token = create_token(TokenModel, user, NormalUserSerializer)
            sendemail.MailTest.certification_mail(user.username, token.key)
        else:
            raise customexception.ValidationException('Normal user required Password')

        return user


class NormalLoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    class Meta:
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_object = authenticate(username=username, password=password)
        if user_object is None:
            raise customexception.AuthenticateException('ID 혹은 Password가 틀렸거나 해당 ID가 존재하지 않습니다.')
        elif user_object.is_active == False:
            raise customexception.AuthenticateException('Email이 인증되지 않았습니다.')
        else:
            return user_object


class LogoutSerializer(serializers.Serializer):
    pass
