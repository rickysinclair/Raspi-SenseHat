from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

i = 0
temp = []
humid = []
press = []

while True:

    temp.append(sense.get_temperature())
    humid.append(sense.get_humidity())
    press.append(sense.get_pressure())

    i+=1
    sleep(1)
    if i == 10:
        break
    
for x in range(len(temp)):
    print("Temperature: {0:4.2f}   Humidity: {1}  Pressure: {2}".format(temp[x],
                                                                 humid[x],
                                                                 press[x]))
