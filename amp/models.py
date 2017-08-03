from django.db import models

# Create your models here.
class Playlist(models.Model):
    playlist_id = models.TextField(unique=True)
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=200, default = "")
    num_tracks = models.IntegerField(default=0)

class Song(models.Model):
    playlist_id= models.TextField()
    artist = models.CharField(max_length=80)
    title = models.CharField(max_length=400)
