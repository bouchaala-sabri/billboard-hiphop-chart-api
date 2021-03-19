import json
import billboard
import falcon

class TopSongs(object):

    def on_get(self, req, resp):
        chart = billboard.ChartData('rap-song')
        resp.body = chart.json()
 