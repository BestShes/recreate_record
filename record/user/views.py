from rest_auth.app_settings import create_token
from rest_auth.models import TokenModel
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.serializers import NormalUserSerializer, NormalLoginSerializer
from .models import Member


class UserViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = NormalUserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.AllowAny,)


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
