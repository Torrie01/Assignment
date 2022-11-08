from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Artiste, Song, Lyrics
from .serializers import ArtisteSerializer, SongSerializer, LyricsSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hey! this is a music app")
    
class ArtisteViewSet(viewsets.ModelViewSet):
        queryset = Artiste.objects.all()
        serializer_class = ArtisteSerializer

class SongViewSet(viewsets.ModelViewSet):
        queryset = Song.objects.all()
        serializer_class = SongSerializer

class LyricsViewSet(viewsets.ModelViewSet):
        queryset = Lyrics.objects.all()
        serializer_class = LyricsSerializer  