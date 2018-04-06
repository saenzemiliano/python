from django.contrib.auth.models import User, Group
from .models import Musician, Album, Track
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'album', 'order', 'title', 'duration')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'artist', 'release_date', 'num_stars', 'tracks')


class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ('id', 'first_name', 'last_name', 'instrument', 'albums')
