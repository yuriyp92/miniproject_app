import machine
import tcs34725
import time

i2c = machine.I2C(1, sda = machine.Pin(26), scl = machine.Pin(32), freq = 400000)
print(i2c.scan())

sensor = tcs34725.TCS34725(i2c)
sensor.gain(16)
sensor.integration_cycles(tcs34725)

while True:
    rgb = sensor.read_rgb()
    print(rgb)
    time.sleep_ms(500)