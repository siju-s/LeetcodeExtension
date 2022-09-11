# serializers.py
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    # avatar = serializers.Field('image.url')
    avatar = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=60)
    username = serializers.CharField(max_length=60)
    rank = serializers.IntegerField(default=0)
    views = serializers.IntegerField(default=0)

    def get_avatar(self, car):
        request = self.context.get('request')
        photo_url = car.avatar
        return request.build_absolute_uri(photo_url)

class QuestionSerializer(serializers.Serializer):
    easyCount = serializers.IntegerField(default=0)
    mediumCount = serializers.IntegerField(default=0)
    hardCount = serializers.IntegerField(default=0)
    totalCount = serializers.IntegerField(default=0)
    easySolvedCount = serializers.IntegerField(default=0)
    mediumSolvedCount = serializers.IntegerField(default=0)
    hardSolvedCount = serializers.IntegerField(default=0)
    totalSolvedCount = serializers.IntegerField(default=0)



