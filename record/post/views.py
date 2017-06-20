from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer, PhotoSerializer
from .models import Post, Photo


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
