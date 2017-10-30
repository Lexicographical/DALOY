from flask import Flask
import json

temp = 28.2
hum = 78.5
pressure = 980.2
alt = 50
app = Flask("Daloy")


@app.route("/")
def hello():
	return json.dumps({"temperature": temp, "humidity": hum, "pressure": pressure, "altitude": alt});

if __name__ == "__main__":
	app.run(host = "127.0.0.1")