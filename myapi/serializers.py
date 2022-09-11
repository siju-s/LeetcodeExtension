# serializers.py
from rest_framework import serializers

from .models import User


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'username', 'rank')
