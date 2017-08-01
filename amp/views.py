from django.shortcuts import render, get_object_or_404
from amp.models import Playlist
import spotipy
import spotipy.util as util
from social_django.models import UserSocialAuth


def index (request) :
    user = request.user
    token = None
    try:
        spotify_login = user.social_auth.get(provider='spotify')
    except UserSocialAuth.DoesNotExist:
        spotify_login = None
    if spotify_login:
        token = spotify_login.extra_data['access_token']
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(user)
        for playlist in playlists['items']:
            p = Playlist()
            p.playlist_id = playlist['id']
            p.username = user
            p.name = playlist['name']
            p.save()
    playlists = Playlist.objects.all()
    return render (request, 'amp/home.html', { 'playlists': playlists})

def profile (request):
    return render (request, 'amp/basic.html', {'content':['Message me to connect','samanthafoster223@gmail.com'] })

def messaging(request) :
    return render (request, 'amp/messaging.html', { 'content': ['Text me  ']})


def playlist(request, pk) :
    playlist = get_object_or_404(Playlist, pk =pk)
    return render (request, 'amp/playlist.html', {'playlist':playlist})
