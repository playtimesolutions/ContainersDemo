#!/usr/bin/python3
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
import os

hostName = "0.0.0.0"
serverPort = 80

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == "/":
			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(bytes(json.dumps(
			{
				'runtime': 'python',
				'hostname': os.uname()[1],
				'dateTimeUtc': datetime.utcnow().isoformat()
			}),"utf-8"))
		else:
 			self.send_response(404)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	if __name__ == "__main__":
		webServer = HTTPServer((hostName, serverPort), Handler)
	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass
	webServer.server_close()