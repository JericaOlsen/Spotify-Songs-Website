import sys
path = '/home/JericaO/SpotifyTopTracks'  # Update with your actual folder path
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application  # Now it should work if app.py is in myproject folder
