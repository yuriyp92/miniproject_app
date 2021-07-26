# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import credentials
import time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
print(wifi.scan())
wifi.connect(credentials.SSID, credentials.PASS)
print("conectando...")
while not wifi.isconnected():
    time.sleep_ms(100)

print("conectado con ip {}".format(wifi.ifconfig()[0]))