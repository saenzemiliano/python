from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import Musician, Album, Track
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, MusicianSerializer, AlbumSerializer, TrackSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer