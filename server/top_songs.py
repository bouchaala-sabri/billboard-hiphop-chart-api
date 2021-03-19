import json
import billboard
import falcon

class TopSongs(object):

    def on_get(self, req, resp):
        songs = []

        chart = billboard.ChartData('rap-song')

        for entry in chart:
            song = {}
            song['title'] = entry.title
            song['image']  = entry.image
            songs.append(song)

        # Create a JSON representation of the resource
        resp.body = json.dumps(songs, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
