from django.db import transaction
from rest_framework import status
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from .models import Artist, Album, Song
from .serializers import *

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['listened', '-listened']
    search_fields = ['title', 'album__artist__name']

    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with transaction.atomic():
            song.listened += 1
            song.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:10]
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)
        return Response(serializer.data)

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

