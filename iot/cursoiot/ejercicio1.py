import machine
import time
import micropython

boton_pulsado = False
def imprimir_msg_error(cosa):
    print("este es un mensaje de error")

def boton_cb(ins):
    micropython.schedule(imprimir_msg_error, None)

boton = machine.Pin(39, machine.Pin.IN)
boton.irq(boton_cb, machine.Pin.IRQ_FALLING)
while True:
    print("-", end="")
    time.sleep_ms(100)