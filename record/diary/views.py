from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Diary
from .serializers import DiarySerializer


class DiaryViewSet(ModelViewSet):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (permissions.AllowAny,)

