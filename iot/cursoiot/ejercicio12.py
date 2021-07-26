from machine import Pin
import esp32
import time

gp = esp32.RMT(0, pin = Pin(27, Pin.OUT), clock_div = 8) #100ns

T0H = 4
T0L = 8
T1H = 7
T1L = 6

uno = (T1H, T1L)
cero = (T0H, T0L)

green = cero + uno + uno + cero + uno + cero + cero + cero
red = uno + uno + uno + uno + uno + uno + uno + uno
blue = 8 * uno

gp.write_pulses(green + red + blue, start = 1)
time.sleep_us(50)
gp.write_pulses(green + red + blue, start = 1)