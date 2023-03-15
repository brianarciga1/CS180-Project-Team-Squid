import spotipy
from flask import session, request, redirect
from spotipy.oauth2 import SpotifyOAuth
import os

os.environ["SPOTIPY_CLIENT_ID"] = "6b908b892b1c4f51aa4286c3d3c66cd0"
os.environ["SPOTIPY_CLIENT_SECRET"] = "171f29c1ee1746828049c3feac06c06e"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8800/auth"

scope = "user-library-read playlist-modify-public"

class get_sp_token():
    # We only need to run this function to get the token, remember to delete '.cache' before running this funcion
    # whole url is doable
    # 1 remaining question: how can we get the code from the browser?
    # let the user copy and paste it?
    def get_sp_token(self):
        cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
        auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scope, cache_handler=cache_handler,show_dialog=True)

        if request.args.get("code"):
            auth_manager.get_access_token(request.args.get("code"))
            return 'access code made'

        if not auth_manager.validate_token(cache_handler.get_cached_token()):
            auth_url = auth_manager.get_authorize_url()
            return auth_url