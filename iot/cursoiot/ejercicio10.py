from umqtt.simple import MQTTClient
import time
from machine import Timer
import machine

MQTT_BROCKER = "broker.hivemq.com"

def mqtt_cb(topic, msg):
    print("{}:{}".format(topic, msg))

client = MQTTClient("ESP3227111992hgfdh", MQTT_BROCKER)
client.set_callback(mqtt_cb)
client.connect()
client.subscribe(b"temp34")
client.subscribe(b"planta_baja/habitacion.temp")

boton = machine.Pin(39, machine.Pin.IN)

#hay_que_enviar = False

#def enviar_msg(x):
#    global hay_que_enviar
#    hay_que_enviar = True

#tim1 = Timer(-1)
#tim1.init(period = 1000, mode = Timer.PERIODIC, callback=enviar_msg)

#proximo_envio = time.ticks_ms() + 1000

while True:
    client.check_msg()
    time.sleep_ms(10)
    if not boton.value():
        client.publish(b"curso_eoi", b"hola soy Yuriy. Prueba boton")

    #print("enviando...")
    #if hay_que_enviar:
    #    client.publish(b"curso_eoi", b"hola soy Yuriy")
    #    hay_que_enviar = False