from .models import Artiste, Song, Lyric
from rest_framework import routers, serializers, viewsets
from .serializers import LyricSerializer, ArtisteSerializer, SongSerializer


class ArtisteListApiView(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    

class SongListApiView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    

class LyricListApiView(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
