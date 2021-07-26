import machine
import time

led = machine.Pin(33, machine.Pin.OUT)
led_pwm = machine.PWM(led, freq = 1000) #convierte el led analógico en digital

while True:
    for i in range(1023):
        led_pwm.duty(i)
        time.sleep_ms(5)