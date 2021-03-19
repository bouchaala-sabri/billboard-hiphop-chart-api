import falcon
from .top_songs import TopSongs
from .top_albums import TopAlbums

api = application = falcon.API()
songs = TopSongs()
albums = TopAlbums()
api.add_route('/top-songs', songs)
api.add_route('/top-albums', albums)