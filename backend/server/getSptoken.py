import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

os.environ["SPOTIPY_CLIENT_ID"] = "9710c9b2411949cf855b1a8da06d1c11"
os.environ["SPOTIPY_CLIENT_SECRET"] = "ba49835923ae4147aec9069a91017efd"
os.environ["SPOTIPY_REDIRECT_URI"] = "https://www.google.com/"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])