from dotenv import load_dotenv
import os, spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="user-read-private"
    )
)

user = sp.current_user()
print(user)

print(user["display_name"])
print(user["id"])

results = sp.search(q = 'One Dance', type = 'track')
track = results["tracks"]["items"][0]

print("Song:", track["name"])
print("Artist:", track["artists"][0]["name"])
print("Spotify URL:", track["external_urls"]["spotify"])
print("Album:", track["album"]["name"])
print("Cover:", track["album"]["images"][0]["url"])
#cover 0,1,2 decreasing size of album cover