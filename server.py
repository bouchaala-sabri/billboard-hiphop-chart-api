import os
import http.server
import socketserver
import billboard
import json

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		self.send_response(HTTPStatus.OK)
		self.end_headers()
		songs = []

		chart = billboard.ChartData('r-b-hip-hop-songs')

		for entry in chart:
			song = {}
			song['title'] = entry.title
			song['image']  = entry.image
			songs.append(song)

		self.wfile.write(json.dumps(songs).encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
