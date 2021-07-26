from p4cox import P4cox
from curso import Led

app = P4cox()
led = Led(27)

def home(x):
    return("index.html")

def encender(x):
    led.on()
    return("index.html")

def info(x):
    return("informacion.html")

app.add_view("/", home)
app.add_view("/encender", encender)
app.add_view("/info", info)
app.add_view("/help", info)

app.run()