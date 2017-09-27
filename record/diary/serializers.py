from rest_framework import serializers

from post.serializers import PostSerializer
from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    post = PostSerializer(many=True, read_only=True, source='post_set')

    class Meta:
        model = Diary
        fields = (
            'author',
            'title',
            'cover_img',
            'travel_area',
            'travel_start_date',
            'travel_end_date',
            'created_date',
            'modified_date',
            'post'
        )

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        diary = self.Meta.model.objects.create(author_id=user_id,
                                               **validated_data)
        return diary

