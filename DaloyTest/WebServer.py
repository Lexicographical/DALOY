from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from threading import Thread

class WebServer:
	def initServer(self):
		print("Starting Web Server")
		thread = Thread(target = self.run)
		thread.start()
		print("Running Web Server")

	def run(self):
		server_address = ("0.0.0.0", 2626)
		self.handler = HTTPServer(server_address, RequestHandler)
		self.handler.serve_forever()


class RequestHandler (BaseHTTPRequestHandler):
	def do_GET(self):
		import DaloyGround
		print(self.path)
		self.send_response(200)
		self.send_header("content-type", "text-plain")
		self.end_headers()
		if self.path == "/":
			self.wfile.write(str.encode("Hello World!"))
		elif self.path == "/daloy/latest":
			self.wfile.write(str.encode(json.dumps(DaloyGround.instance.getLatestEntry())))
		elif self.path == "/daloy/all":
			self.wfile.write(str.encode(json.dumps(DaloyGround.instance.getAllEntries())))
