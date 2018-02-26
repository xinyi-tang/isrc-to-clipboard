import sys
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
 
SPOTIPY_CLIENT_ID = 'your client id'
SPOTIPY_CLIENT_SECRET = 'your client secret'
 
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
 
inp = "{query}"
 
track = sp.track(inp)
isrc = track["external_ids"]["isrc"]
 
cmd = 'echo %s | tr -d "\n" | pbcopy' % isrc
os.system(cmd)
