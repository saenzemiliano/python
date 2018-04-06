from django.contrib.auth.models import User, Group
from .models import Musician, Album, Track
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = ('first_name', 'last_name', 'instrument')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = ('artist', 'name', 'release_date', 'num_stars', 'tracks')


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('album', 'order', 'title', 'duration')

