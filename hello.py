import time
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Los!")
sense.clear()
sense.load_image("s.png")
humidity = sense.get_humidity()
#sense.show_message("Luftfeuchtigkeit: %s %%rH" % humidity)
print("Luftfeuchtigkeit: %s %%rH" % humidity)
temp = sense.get_temperature()
#sense.show_message("Temperatur: %s C" % temp)
print("Temperatur: %s C" % temp)
temp = sense.get_temperature_from_humidity()
#sense.show_message("Temperatur-Feuchtigkeit: %s C" % temp)
print("Temperatur-Feuchtigkeit: %2.2f C" % temp)    # %2.2f Wert als Floatingpoint mit 2 vor und 2 nach dem Komma
temp = sense.get_temperature_from_pressure()
#sense.show_message("Temperatur-Druck: %s C" % temp)
print("Temperatur-Druck: %s C" % temp)
pressure = sense.get_pressure()
#sense.show_message("Druck: %s Millibars" % pressure)
print("Druck: %s Millibars" % pressure)
sense.set_imu_config(True, False, False)  # nur Kompass an / nicht Neigungssensor und nicht Beschleunigungsssensor
for i in range(1,10):  #for i=1 i<10 i++
    sense.show_message ( "%s" % i )    # %s Wert als String ausgeben
	north = sense.get_compass()
    print("North: %s" % north)
    time.sleep(1)
sense.clear()	
print("Temperatur: %s C" % temp)