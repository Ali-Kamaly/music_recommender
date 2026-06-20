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
