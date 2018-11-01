from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from threading import Thread
import Constants

class WebServer:
	def initServer(self):
		thread = Thread(target = self.run)
		thread.start()

	def run(self):
		server_address = ("0.0.0.0", 2626)
		self.handler = HTTPServer(server_address, RequestHandler)
		self.handler.serve_forever()


class RequestHandler (BaseHTTPRequestHandler):
	def do_GET(self):
		import DaloyGround
		self.send_response(200)
		self.send_header("content-type", "text-plain")
		self.end_headers()
		if self.path == "/":
			self.wfile.write(str.encode("Hello World!"))
		elif self.path == "/daloy/hangin/latest":
			self.wfile.write(str.encode(json.dumps(DaloyGround.instance.getLatestEntry(type=0))))
		elif self.path == "/daloy/hangin/all":
			self.wfile.write(str.encode(json.dumps(DaloyGround.instance.getAllEntries(type=0))))
		elif self.path == "/daloy/tubig/latest":
			self.wfile.write(str.encode(json.dumps(DaloyGround.instance.getLatestEntry(type=1))))
		elif self.path == "/daloy/tubig/all":
			self.wfile.write(str.encode(json.dumps(DaloyGround.instance.getAllEntries(type=1))))
		elif self.path == "/daloy/tubig/open":
		    self.wfile.write("Opening solenoid valve")
		    Constants.relay = "Open"
		    relayChanged = True
	    elif self.path == "/daloy/tubig/close":
	        self.wfile.write("Closing solenoid valve")
	        Constants.relay = "Close"
	        relayChanged = True
		elif self.path.startsWith("/daloy/tubig/rate/")
			rate = self.path[18:]
			try:
				Constants.rate = int(rate)
			except ValueError:
				print("Invalid rate found: " + str(rate))
			
