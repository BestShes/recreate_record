from rest_framework import filters
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Diary
from .serializers import DiarySerializer


class DiaryViewSet(ModelViewSet):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all().order_by('-created_date')
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

