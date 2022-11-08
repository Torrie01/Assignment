from turtle import title
from django.db import models
from datetime import datetime

class Artiste(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 400)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"

 

class Song(models.Model):
    artiste=models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    date_released = models.DateTimeField(max_length = 50)
    likes = models.CharField(max_length = 120);
    # Artiste_id = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.title}"
    
class Lyrics(models.Model):
    songs=models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.CharField(max_length = 3000)
    song_id = models.CharField(max_length = 100)

    def __str__(self):
        if len(self.content) > 50:
            return f"{self.content[0:50]}..."
        else:
            return f"{self.content}"
  