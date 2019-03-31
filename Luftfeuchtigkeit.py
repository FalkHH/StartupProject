import time                      # importieren einer gesamten Standard-Bilbliothek 
from sense_hat import SenseHat   # importieren einer Klasse aus spezieller Bilbliothek
sensor = SenseHat()              # Instanz vom Objektklasse erstellt

def LuftfeuchtigkeitMessen(Dateiname="Feuchtigkeitsdaten"):    #Funktion nutzt Standard-Datei, falls sie ohne speziellem Parameter aufgerufen wird
	"""Misst die Luftfeuchtigkeit der Umgebung und schreibt den Wert in eine CSV-Datei
	"""
	Feuchtigkeit = sensor.get_humidity()                  # misst die Luftfeuchtigkeit
	Zeit = time.time()                                    # 'Zeitstempel als Wert
	F_out  = open(Dateiname + ".csv", "a")                # Offenen einer Datei zum Datenanhängen
	F_out.write("%s,%2.2f\n" % (Zeit,Feuchtigkeit) )      # Datei mit Werten s=Sting f=Floatingpoint beschreiben  \n = Zeilenumbruch
	F_out.close()                                         # Datei schließen
	sensor.show_message("%2.2f %%rH" % Feuchtigkeit)   # %% ermöglicht die Anzeige eines %	

i = 1
while True:
	Datum = time.strftime("%y-%m-%d")                             # Datum feststellen
	LuftfeuchtigkeitMessen("Feuchtigkeitsdaten_%s.csv" % (Datum))
	time.sleep(30)				                                  # 30 Sekunden warten
	i += 1
	if i > 10 :
		break		                                              # While-Scheife verlassen
		
		
	

