from rest_framework import serializers

from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'author',
            'title',
            'cover_img',
            'created_date',
            'modified_date'
        )
