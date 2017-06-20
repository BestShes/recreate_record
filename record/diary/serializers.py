from rest_framework import serializers

from post.serializers import PostSerializer
from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True, source='post_set')

    class Meta:
        model = Diary
        fields = (
            'author',
            'title',
            'cover_img',
            'created_date',
            'modified_date',
            'post'
        )
