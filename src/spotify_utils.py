from dotenv import load_dotenv
import os, spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="user-read-private"
    )
)

def search_track(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q = query, type = 'track')
    items = results["tracks"]["items"]
    if len(items)==0:
        return 
    track = results["tracks"]["items"][0]

    song_name = track["name"]
    artist = track["artists"][0]["name"]
    spotify_url = track["external_urls"]["spotify"]
    album = track["album"]["name"]
    cover = track["album"]["images"][0]["url"]

    return spotify_url, album, cover

def extract_track_id(spotify_url):
    if "track/" not in spotify_url:
        print("not valid")
        return None
    
    track_id = spotify_url.split('track/')[1].split('?')[0]
    return track_id


def get_track_from_url(spotify_url):
    track_id = extract_track_id(spotify_url)
    print(track_id)
    if track_id is None:
        return None
    
    track = sp.track(track_id)
    track_name = track['name']
    artists = ';'.join([artist['name'] for artist in track['artists']])
    print(track_name, artists)
    return track_name, artists

get_track_from_url("https://open.spotify.com/track/6DCZcSspjsKoFjzjrWoCdn")