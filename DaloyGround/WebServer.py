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
			temp = hum = pressure = alt = 0
			return json.dumps({"temperature": temp, "humidity": hum, "pressure": pressure, "altitude": alt});