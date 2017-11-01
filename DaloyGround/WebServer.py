import DaloyGround
from flask import Flask
import json

appname = "Daloy"

class WebServer:
	def __init__(self):
		self.app = Flask(appname)

	def initServer(self):
		global instance
		@app.route("/")
		def index():
			return """<h1>Project Daloy Web Server</h1>"""
		@app.route("/daloy/latest")
		def index():
			temp, hum, pressure, alt = DaloyGround.instance.getLatestEntry()
			return json.dumps({"temperature": temp, "humidity": hum, "pressure": pressure, "altitude": alt});
		@app.route("/daloy/all")
		def index():
			entries = DaloyGround.instance.getAllEntries()
			return json.dumps(entries)