
<h1>Project Daloy<br>
<strong>D</strong>rone-based depth and <strong>A</strong>tmospheric <strong>L</strong>evel <strong>O</strong>pen-source monitoring device for the Filipino <strong>Y</strong>outh</h1>
<p>Git Repository for code and other resources related to the development of <strong>Project Daloy</strong>, the official entry of PSHS-CVisC to <strong>InnoBox: Search for the Most Innovative Teaching and Learning Resources in Science</strong></p>
<h1>Parts used</h1>
<ul>
	<li>Arduino Uno</li>
	<li>Raspberry Pi</li>
	<li>XBee Shield</li>
	<li>DHT22</li>
	<li>BMP180</li>
	<li>MPU6050 Gyroscope</li>
</ul>
<h1>Materials List and Budgetary Requirements</h1>
<table>
	<tr>
		<td colspan="4" style="text-align: center"><strong>Daloy Air (Drone)</strong></td>
	</tr>
	<tr>
		<td><strong>Material</strong></td>
		<td><strong>Unit Cost</strong></td>
		<td><strong>Quantity</strong></td>
		<td><strong>Price</strong></td>
	</tr>
	<tr>
		<td>Arduino Nano</td>
		<td>350</td>
		<td>2</td>
		<td>1050</td>
	</tr>
	<tr>
		<td>NRF24L01</td>
		<td>100</td>
		<td>2</td>
		<td>200</td>
	</tr>
	<tr>
		<td>Multiwii Flight Controller</td>
		<td>1500</td>
		<td>1</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>DHT-22 Humidity</td>
		<td>350</td>
		<td>1</td>
		<td>350</td>
	</tr>
	<tr>
		<td>BMP180 Barometric + Temp</td>
		<td>300</td>
		<td>1</td>
		<td>300</td>
	</tr>
	<tr>
		<td>Camera</td>
		<td>???</td>
		<td>1</td>
		<td>???</td>
	</tr>
	<tr>
		<td>Electronic Brushless Motor Speed Controller ESC</td>
		<td>1800</td>
		<td>4</td>
		<td>7200</td>
	</tr>
	<tr>
		<td>Brushless Motors</td>
		<td>700</td>
		<td>4</td>
		<td>2800</td>
	</tr>
	<tr>
		<td>Case / Body</td>
		<td>2000</td>
		<td>1</td>
		<td>2000</td>
	</tr>
	<tr>
		<td>Li-Po Battery 7.4V / 11.1V</td>
		<td>330</td>
		<td>1</td>
		<td>330</td>
	</tr>
	<tr>
		<td colspan="2" style="text-align: center"><strong>Subtotal</strong></td>
		<td colspan="2" style="text-align: right">15730</td>
	</tr>
</table>
<table>
	<tr>
		<td colspan="4" style="text-align: center"><strong>Daloy Ground (Main)</strong></td>
	</tr>
	<tr>
		<td><strong>Material</strong></td>
		<td><strong>Unit Cost</strong></td>
		<td><strong>Quantity</strong></td>
		<td><strong>Price</strong></td>
	</tr>
	<tr>
		<td>Raspberry Pi 3</td>
		<td>2400</td>
		<td>1</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>NRF24L01</td>
		<td>100</td>
		<td>1</td>
		<td>100</td>
	</tr>
	<tr>
		<td>Solar Panel</td>
		<td>2000</td>
		<td>1</td>
		<td>2000</td>
	</tr>
	<tr>
		<td>Charging Station</td>
		<td>???</td>
		<td>1</td>
		<td>???</td>
	</tr>
	<tr>
		<td>Case / Body</td>
		<td>1000</td>
		<td>1</td>
		<td>1000</td>
	</tr>
	<tr>
		<td colspan="2" style="text-align: center"><strong>Subtotal</strong></td>
		<td colspan="2" style="text-align: right">5500</td>
	</tr>
</table>
<table>
	<tr>
		<td colspan="4" style="text-align: center"><strong>Controller</strong></td>
	</tr>
	<tr>
		<td><strong>Material</strong></td>
		<td><strong>Unit Cost</strong></td>
		<td><strong>Quantity</strong></td>
		<td><strong>Price</strong></td>
	</tr>
	<tr>
		<td>Arduino Nano</td>
		<td>350</td>
		<td>1</td>
		<td>350</td>
	</tr>
	<tr>
		<td>NRF24L01</td>
		<td>100</td>
		<td>1</td>
		<td>100</td>
	</tr>
	<tr>
		<td>Li-Po Battery 7.4V / 11.1V</td>
		<td>330</td>
		<td>1</td>
		<td>330</td>
	</tr>
	<tr>
		<td colspan="2" style="text-align: center"><strong>Subtotal</strong></td>
		<td colspan="2" style="text-align: right">780</td>
	</tr>
</table>

# Total: 22010

<h1>Software/Libraries used</h1>
<table>
	<tr>
		<td colspan="2" style="text-align: center"><strong>Drone Box</strong></td>
	</tr>
	<tr>
		<td><strong>Library</strong></td>
		<td><strong>Source</strong></td>
	</tr>
	<tr>
		<td>Arduino.h</td>
		<td>Arduino built-in</td>
	</tr>
	<tr>
		<td>Wire.h</td>
		<td>Arduino built-in</td>
	</tr>
	<tr>
		<td>Adafruit_Sensor.h</td>
		<td>Adafruit BMP085 Library</td>
	</tr>
	<tr>
		<td>Adafruit_BMP085_U.h</td>
		<td>Adafruit BMP085 Unified</td>
	</tr>
	<tr>
		<td>DHT.h</td>
		<td>DHT Sensor Library</td>
	</tr>
</table>
<h1>Proposed Design</h1>
![](Project Daloy.png)