import json
import billboard
import falcon

class TopAlbums(object):

    def on_get(self, req, resp):
        albums = []

        chart = billboard.ChartData('rap-albums')

        for entry in chart:
            album = {}
            album['title'] = entry.title
            album['image']  = entry.image
            albums.append(album)

        # Create a JSON representation of the resource
        resp.body = json.dumps(albums, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
