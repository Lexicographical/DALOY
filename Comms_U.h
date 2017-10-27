#ifndef COMMS_U
#define COMMS_U

Comms::Comms() {
  this->server = &ESP8266WebServer(80);
  Wifi.begin(this->ssid, this->password);
  while (Wifi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting...");
  }
  Serial.print("IP Address: ");
  Serial.println(Wifi.localIP());

  this->server->on("daloyweb", Comms::webHandler);
  this->server->begin();
}

static Comms Comms::getInstance() {
  if (instance == 0) {
    instance = &Comms();
  }
  return instance;
}

void Comms::handleClient() {
  this->server->handleClient();
}

void Comms::webHandler() {
   if (!server.hasArg("body")) {
     server.send(200, "text/plain", "No message received!");
     return;
   }

   String message = "Received:\n";
   message += server.arg("body");
   message += "\n";

   server.send(200, "text/plain", message);
   Serial.println(message);
}


#endif
