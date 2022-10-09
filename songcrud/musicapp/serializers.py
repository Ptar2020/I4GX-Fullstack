from rest_framework import serializers
from .models import Artiste, Song, Lyric



class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['url','content', 'song_id']
        

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['url','first_name', 'last_name', 'age'] 


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['url', 'title', 'date_released', 'artiste_id', 'likes']