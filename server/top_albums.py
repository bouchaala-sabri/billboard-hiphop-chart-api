import json
import billboard
import falcon

class TopAlbums(object):

    def on_get(self, req, resp):
        chart = billboard.ChartData('rap-albums')
        resp.body = chart.json()
