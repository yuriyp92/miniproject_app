import os
import time
import random

print(os.listdir())

#with open("sensor.csv", "a") as f:
#    f.write("timestamp, temperatura \n")
#    for i in range (5):
#        timestamp = time.ticks_ms()
#        temp = random.randint(15,33)
#        f.write("{}, {}\n".format(timestamp, temp))
    
with open("sensor.csv", 'r') as f:
    print(f.read())
