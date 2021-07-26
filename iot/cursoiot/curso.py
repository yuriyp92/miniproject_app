import machine
import neopixel

class Led:
    def __init__(self, pin):
        self.np = neopixel.NeoPixel(machine.Pin(pin),1)
        self._estado_led = False
        self.tim = machine.Timer(-1)
        self.color = (100,100,100)
    
    def on(self):
        self.np[0] = (255,255,255)
        self.np.write()
        self._estado_led = True

    def off(self, *args):
        self.np[0] = (0,0,0)
        self.np.write()
        self._estado_led = False
    
    def value(self):
        return self.estado_le
    
    def flash(self):
        self.on()
        self.tim.init(period = 200, mode = machine.Timer.ONE_SHOT, callback = self.off)
    
    def set_color(self, red, green, blue):
        self.color = (red, green, blue)
