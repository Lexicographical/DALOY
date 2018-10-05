from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from threading import Thread

class WebServer:
	def initServer(self):
		thread = Thread(target = self.run)
		thread.start()

	def run(self):
		server_address = ("", 2626)
		self.handler = HTTPServer(server_address, RequestHandler)
		self.handler.serve_forever()


class RequestHandler (BaseHTTPRequestHandler):
	def do_GET(self):
		import Constants
		self.send_response(200)
		self.send_header("content-type", "text-plain")
		self.end_headers()
		if self.path == "/":
			self.wfile.write(str.encode("Hello World!"))
		elif self.path == "/daloy/latest":
			self.wfile.write(str.encode(json.dumps(Constants.instance.getLatestEntry())))
		elif self.path == "/daloy/all":
			self.wfile.write(str.encode(json.dumps(Constants.instance.getAllEntries())))
