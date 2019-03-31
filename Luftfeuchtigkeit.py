import time                      # importieren einer gesamten Standard-Bilbliothek 
import os
from sense_hat import SenseHat   # importieren einer Klasse aus spezieller Bilbliothek
sensor = SenseHat()              # Instanz vom Objektklasse erstellt



def LuftfeuchtigkeitMessen(Dateiname="Feuchtigkeitsdaten"):    #Funktion nutzt Standard-Datei, falls sie ohne speziellem Parameter aufgerufen wird
	"""Misst die Luftfeuchtigkeit der Umgebung und schreibt den Wert in eine CSV-Datei
	"""
	Feuchtigkeit = sensor.get_humidity()                  # misst die Luftfeuchtigkeit
	sense.show_message("Luftfeuchtigkeit: %s %%rH" % Feuchtigkeit)   # %% ermöglicht die Anzeige eines %
	Zeit = time.time()                                    # 'Zeitstempel als Wert
	F_out  = open(Dateiname + ".csv", "a")                # Offenen einer Datei zum Datenanhängen
	F_out.write("%s,%2.2f\n" % (Zeit,Feuchtigkeit) )      # Datei mit Werten s=Sting f=Floatingpoint beschreiben  \n = Zeilenumbruch
	F_out.close()                                         # Datei schließen  

def DateiUmbenennen(Dateiname="Feuchtigkeitsdaten"):
	"""Benennt eine Datei um, indem ein Zeitstempel hinten am Namen angehängt wird
	"""
	Zeit = time.now()     # Zeitstempel als STring
	os.rename("%s.csv" % Dateiname,"%s_%s.csv" % (Dateiname,Zeit))

Tag_alt = time.strftime("%d")     # aktuellen Monatstag festlegen
i = 1
while True:
	LuftfeuchtigkeitMessen()
	time.sleep(30)				# 30 Sekunden warten
	Tag_neu = time.strftime("%d")   # Monatstag feststellen
	if Tag_neu != Tag_alt :
		DateiUmbenennen()
		Tag_alt = Tag_neu
	i += 1
	if i > 10 :
		break		# While-Scheife verlassen
		
		
	

