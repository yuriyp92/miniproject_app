from machine import Timer
import time

def alerta(e):
    print("ha saltado la alarma")

timA = Timer(0)
timB = Timer(-1)

timA.init(period = 2000, mode = Timer.ONE_SHOT, callback = alerta)
timB.init(period = 500, mode = Timer.PERIODIC, callback = lambda e:print("Timer B"))

for i in range(5):
    print(i)
    time.sleep(1)
timB.deinit()