from curso import Led
import machine
import time
import network
import socket
import esp32

led = Led(27)

def getHtmlContent(temp):
    #if led.value():
    #    estado_led_str = "encendido"
    #else:
    #    estado_led_str = "apagado"
    estado_led_str = "encendido" if led.value() else "apagado"
    return """<html><head> <title>Ejemplo 1</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:;base64,iVBORw0KGgo="><style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>CONTROL DE LED</h1> 
    <p>Temperatura: """ + str(temp) +""" F</p>
    <p>El led esta """ + estado_led_str + """</p>
    <p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""

wifi = network.WLAN(network.AP_IF)
wifi.config(essid="miESP")
wifi.active(True)
print(wifi.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ("0.0.0.0", 80) )
s.listen(5)

while True:
    print("esperando conexion....")
    conn, addr = s.accept()
    print(addr)
    request = conn.recv(1024)
    request_str = request.decode()
    print(str)
    if request_str.find("GET /?led=on") != -1:
        print("se encontro led on")
        led.on()
    elif request_str.find("GET /?led=off") != -1:
        print("se encontro led off")
        led.off()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-Type: text/html\n")
    conn.send("Connection: close\n\n")
    temp = esp32.raw_temperature()
    conn.sendall(getHtmlContent(temp))
    conn.close()