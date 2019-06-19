from sense_hat import SenseHat
import time
from guizero import App, Text, Picture

sense = SenseHat()
app = App("Weather Station")

def display():
    timeDis.value = time.strftime("%H:%M:%S")
    dateDis.value = time.strftime("%a, %d %b %Y")
    tempDis.value = "Temperature: {0:4.2f}".format(sense.get_temperature())
    humidDis.value = "Humidity: {0:4.2f}".format(sense.get_humidity())
    pressDis.value = "Pressure: {0:4.2f}".format(sense.get_pressure())

timeDis = Text(app, size=20, font="Consolas")

dateDis = Text(app, size=20, font="Consolas")

tempPic = Picture(app, image="/home/pi/Desktop/images/thermo.png", height=100, width=100)
tempDis = Text(app, size=20, font="Consolas")

humidPic = Picture(app, image="/home/pi/Desktop/images/humid.png", height=100, width=100)
humidDis = Text(app, size=20, font="Consolas")

pressPic = Picture(app, image="/home/pi/Desktop/images/press.png", height=100, width=100)
pressDis = Text(app, size=20, font="Consolas")

timeDis,dateDis,tempDis,humidDis,pressDis.repeat(100, display)

app.display()
