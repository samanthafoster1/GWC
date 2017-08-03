from django.shortcuts import render, get_object_or_404
from amp.models import Playlist, Song
import spotipy
import spotipy.util as util
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required

@login_required
def index (request) :
    user = request.user

    print(user)
    playlists = []
    spotify_login = None
    token = None
    if user.is_authenticated:
        try:
            if user.social_auth:
                spotify_login = user.social_auth.get(provider='spotify')
        except UserSocialAuth.DoesNotExist:
            spotify_login = None
        if spotify_login:
            token = spotify_login.extra_data['access_token']
        if token:
            sp = spotipy.Spotify(auth=token)
            user = str(user)
            playlists = sp.user_playlists(user)
            for playlist in playlists['items']:
                if playlist['owner']['id']==user:
                    p = Playlist()
                    p.playlist_id = playlist['id']
                    p.username = user
                    p.name = playlist['name']
                    p.num_tracks = playlist['tracks']['total']
                    try:
                        p.save()
                    except:
                        hello = ""
                    results=sp.user_playlist(user,playlist['id'], fields='tracks,next')
                    tracks = results['tracks']
                    show_tracks(tracks, playlist['id'])
                    while tracks['next']:
                        tracks=sp.next(tracks)
                        show_tracks(tracks, playlist['id'])

            playlists = Playlist.objects.all()
    return render (request, 'amp/home.html', { 'playlists': playlists, 'spotify_login': spotify_login})
@login_required
def profile (request):
    user = request.user
    print(user)
    playlists = []
    spotify_login = None
    token = None
    profile = None
    if user.is_authenticated:
        try:
            if user.social_auth:
                spotify_login = user.social_auth.get(provider='spotify')
        except UserSocialAuth.DoesNotExist:
            spotify_login = None
        if spotify_login:
            token = spotify_login.extra_data['access_token']
        if token:
            sp = spotipy.Spotify(auth=token)
            profile = sp.current_user()
    print(profile)
    if sp.current_user()['images']!= []:
        profile_image_url = sp.current_user()['images'][0]['url']
    else:
        profile_image_url = "https://s-media-cache-ak0.pinimg.com/736x/1d/ea/b7/1deab7e6c0b2947a17343d3d0efee99c--notes-music-musical-notes-art.jpg"
    name = profile["display_name"] or profile ["id"]
    spotify_link = profile["external_urls"]["spotify"]
    return render (request, 'amp/basic.html', {'profile': profile, 'name': name, 'profile_image_url': profile_image_url, 'spotify': spotify_link})

def messaging(request) :
    return render (request, 'amp/messaging.html', { 'content': ['Text me  ']})


def playlist(request, pk) :
    playlist = get_object_or_404(Playlist, pk =pk)
    return render (request, 'amp/playlist.html', {'playlist':playlist})

def matches(request) :
    user= request.user
    user=str(user)
    playlists= Playlist.objects.all()
    user_playlist= Playlist.objects.filter(username=user)
    songs=Song.objects.all()
    dictionary={}
    tsil=[]
    for i in user_playlist:
        id1=i.playlist_id
        songs_id1=Song.objects.all().filter(playlist_id=id1)
        for playlist in playlists:
            id2=playlist.playlist_id
            songs_id2=Song.objects.all().filter(playlist_id=id2)
            for song1 in songs_id1:
                for song2 in songs_id2:
                    some_key=id1+' - '+id2
                    if song1.title==song2.title and song1.artist==song2.artist:
                        dictionary[some_key]=dictionary.get(some_key,1)+1
    for key,value in dictionary.items():
        id1=key[:22]
        id2=key[25:]
        playlist1=Playlist.objects.all().filter(playlist_id=id1)
        playlist2=Playlist.objects.all().filter(playlist_id=id2)
        num=min(playlist1[0].num_tracks,playlist2[0].num_tracks)
        if value/num>=.30:
            if playlist2[0].username not in tsil:
                if playlist2[0].username != user:
                    tsil.append(playlist2[0].username)
    print(tsil)
    return render(request,'amp/display.html',{'matches':tsil})

def show_tracks(tracks, r) :
    for i, item in enumerate(tracks['items']):
        track = item['track']
        s=Song()
        s.playlist_id= r
        s.name=track['name']
        s.artist=track['artists'][0]['name']
        s.save()
