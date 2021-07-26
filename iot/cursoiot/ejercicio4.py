from curso import Led
import machine
import time


estado_led = False

def boton_pulsado(cosa):
    global estado_led
    estado_led = not estado_led

led = Led(27)
boton = machine.Pin(39, machine.Pin.IN)
boton.irq(boton_pulsado, machine.Pin.IRQ_FALLING)

while True:
    if estado_led:
        led.on()
    else:
        led.off()
    time.sleep_ms(50)