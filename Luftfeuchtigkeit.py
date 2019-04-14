import time                      # importieren einer gesamten Standard-Bilbliothek 
from sense_hat import SenseHat   # importieren einer Klasse aus spezieller Bilbliothek
sensor = SenseHat()              # Instanz vom Objektklasse erstellt
m = sensor.get_humidity()        # misst ersten Feuchtigkeitswert

a = [m,m,m,m,m,m,m,m]            # initial ist das Array mit dem Iitialwert belegt

def LuftfeuchtigkeitMessen(Dateiname="Feuchtigkeitsdaten"):    #Funktion nutzt Standard-Datei, falls sie ohne speziellem Parameter aufgerufen wird
	"""Misst die Luftfeuchtigkeit der Umgebung und schreibt den Wert in eine CSV-Datei
	"""
	Feuchtigkeit = sensor.get_humidity()                  # misst die Luftfeuchtigkeit
	Zeit = time.time()                                    # 'Zeitstempel als Wert
	F_out  = open(Dateiname + "%s.csv", "a")              # Oeffenen einer Datei zum Datenanhaengen
	F_out.write("%s,%2.2f\n" % (Zeit,Feuchtigkeit) )      # Datei mit Werten s=Sting f=Floatingpoint beschreiben  \n = Zeilenumbruch
	F_out.close()                                         # Datei schliessen
	sensor.show_message("%2.2f %%rH * %2.2f" % (Feuchtigkeit,Feuchtigkeit) )      # %% ermoeglicht die Anzeige eines %
	MesswertSpeichern(Feuchtigkeit)	

del MesswertSpeichern(m)		# schiebt die bislang gespeicherten Werte im Array nach vorne und speichert den neuen Wert ans Ende
	i = 0
	while i < 7:
		a[i] = a[i+1]
		i += 1
		if i = 7:
			a[7] = m

j = 1
while True:
	Datum = time.strftime("%y-%m-%d-%H")                             # Datum mit Stunde feststellen
	LuftfeuchtigkeitMessen("Feuchtigkeitsdaten_%s" % (Datum))
	time.sleep(30)				                                  # 30 Sekunden warten
	j += 1
	if j > 10 :
		break		                                              # While-Scheife unbedingt verlassen
		
		
	

