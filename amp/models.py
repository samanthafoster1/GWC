from django.db import models

# Create your models here.
class Playlist(models.Model):
    playlist_id = models.TextField()
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=200, default = "")
