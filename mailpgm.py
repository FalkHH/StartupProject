import subprocess
from sense_hat import SenseHat
sense = SenseHat()
humidity = sense.get_humidity()

text = "Luftfeuchtigkeit: %s %%rH" % humidity
sense.show_message(text)
print(text)
p1 = subprocess.Popen(['echo', text], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['mail', '-s', '"Test Betreff Mail"', 'falk.wollatz@web.de'], stdin=p1.stdout)

print(p2.stdout)


