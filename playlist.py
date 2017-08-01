import sys
import spotipy
import spotipy.util as util

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        wtf = "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])
playlist_id = []

if __name__ == '__main__':
    username = 'bellamza01'

    token =     'BQDRjado86_5-aAN4VXIeSBLuq7vuvR4kfVvlirCd-sbZ8xWM93Uo9JHPQsZ2rzbzq6kNmtAHCukGjmVRYj7axvh3wsZWqDpMUPRcWsrUflv9cT-j315VyUqjdvF47DvB9aob-pnSbu9N-dTQSU'
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                playlis = playlist['name']
                thing = '  total tracks', playlist['tracks']['total']
                # print(thing)
                playlist_id.append(playlist['id'])

                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
print(playlist_id)
