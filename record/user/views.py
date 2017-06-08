from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from user.serializers import NormalUserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = NormalUserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.AllowAny,)

