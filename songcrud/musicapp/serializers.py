from rest_framework import serializers
from .models import Artiste, Song, Lyrics

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = "__all__"