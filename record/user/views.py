from rest_auth.app_settings import create_token
from rest_auth.models import TokenModel
from rest_framework import filters
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.serializers import NormalUserSerializer, NormalLoginSerializer, LogoutSerializer
from utils import customexception
from .models import Member


class UserViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = NormalUserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


def emailcertification(request):
    try:
        username = request.GET.get('username')
        key = request.GET.get('key')
        user_object = Member.objects.get(username=username)
        if user_object.is_active == False and user_object.auth_token == key:
            user_object.is_active = True
            user_object.save()
        else:
            raise customexception.AuthenticateException
    except:
        raise customexception.AuthenticateException('유효하지 않습니다.')


class LoginView(GenericAPIView):
    serializer_class = NormalLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_object = serializer.save()
        token = create_token(TokenModel, user_object, serializer)
        user = NormalUserSerializer(user_object)
        return Response(status=status.HTTP_200_OK, data={'user': user.data,
                                                         'token': token.key})


class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        TokenModel.objects.get(user=user).delete()
        return Response(status=status.HTTP_200_OK, data={'detail': 'Logout Succeeded'})
