import piexif
from rest_framework import serializers

from .models import Post, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'photo',
            'post',
            'longitude',
            'latitude'
        )

    def create(self, validated_data):
        photo = validated_data['photo']
        location = self.get_gps_location(photo)
        photo = Photo.objects.create(latitude=location[0],
                                     longitude=location[1],
                                     **validated_data)
        return photo

    @staticmethod
    def get_gps_location(photo):
        try:
            exif_dict = piexif.load(photo.read())
            gps_data = exif_dict['GPS']
            latitude = (gps_data[2][0][0]) + (gps_data[2][1][0] / 60 + (gps_data[2][2][0]) / 360000)
            longitude = (gps_data[4][0][0]) + (gps_data[4][1][0] / 60 + (gps_data[4][2][0]) / 360000)
            result = (round(latitude, 4), round(longitude, 4))
        except:
            latitude = None
            longitude = None
            result = (latitude, longitude)

        return result


class PostSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True, source='photo_set')

    class Meta:
        model = Post
        fields = (
            'diary',
            'content',
            'created_date',
            'modified_date',
            'photo',
        )
