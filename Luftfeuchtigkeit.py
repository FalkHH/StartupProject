import time                      # importieren einer gesamten Standard-Bilbliothek 
import numpy as np
from sense_hat import SenseHat   # importieren einer Klasse aus spezieller Bilbliothek
sensor = SenseHat()              # Instanz vom Objektklasse erstellt

m = sensor.get_humidity()        # misst ersten Feuchtigkeitswert
a = [m,m,m,m,m,m,m,m]            # initial ist das Array mit dem Iitialwert belegt
# X = [255, 0, 0]      # Red
# W = [255, 255, 255]  # White
# B = [0, 0, 255]	   # Blau
O = [0, 0, 0]          # Black

def LuftfeuchtigkeitMessen(Dateiname="Feuchtigkeitsdaten"):    #Funktion nutzt Standard-Datei, falls sie ohne speziellem Parameter aufgerufen wird
	"""Misst die Luftfeuchtigkeit der Umgebung und schreibt den Wert in eine CSV-Datei
	"""
	Feuchtigkeit = sensor.get_humidity()                  # misst die Luftfeuchtigkeit
	Zeit = time.time()                                    # 'Zeitstempel als Wert
	F_out  = open(Dateiname + ".csv", "a")                # Oeffenen einer Datei zum Datenanhaengen
	F_out.write("%s,%2.2f\n" % (Zeit,Feuchtigkeit) )      # Datei mit Werten s=Sting f=Floatingpoint beschreiben  \n = Zeilenumbruch
	F_out.close()                                         # Datei schliessen
	# sensor.show_message("%2.2f %%rH * %2.2f" % (Feuchtigkeit,Feuchtigkeit) )      # %% ermoeglicht die Anzeige eines  %
	MesswertSpeichern(Feuchtigkeit)	
	

def MesswertSpeichern(Messwert):		# schiebt die bislang gespeicherten Werte im Array nach vorne und speichert den neuen Wert ans Ende
	i = 0
	while i < 7:
		a[i] = a[i+1]
		i += 1
		if i == 7:
			a[7] = Messwert

def MesswerteNormieren():
	amax = max(a)
	amin = min(a)
	d = amax - amin
	if d == 0:							# alle Werte sind gleich (am Anfang)
		X = FarbwertErmitteln(amin)
		default = [
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		X, X, X, X, X, X, X, X,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O
		]
		return default						# lineare Darstellung
	#b = [int(0.5+(m-amin)*7/d) for m in a]	# Normierung auf Matrixzeilen;  mit 0.5 ind INT gerundet auf Integerwert
	matrix = []								# Anlegen eines Arrays
	for r in range(8):						# r from 0 to 7
		for m in a:							# alle 8 B-Werte ansehen
			b = int(0.5+(m-amin)*7/d)
			if b == 7-r:					# b-Wert auf Zeilenwert ueberpruefen
				matrix.append(FarbwertErmitteln(m))			# alle 64 Farb-Werte nacheinander anhaengen
			else:
				matrix.append(O)
	return matrix

def FarbwertErmitteln(Feuchtigkeit):
	colA = [0,0,255]
	colB = [255,0,0]
	minF = 30
	maxF = 70
	if Feuchtigkeit <= minF:						# 30 und kleiner blau anzeigen
		X = colA
	elif Feuchtigkeit >= maxF:					# 70 und hoeher als rot anzeigen
		X = colB
	else:										# dazwischen die Rot- und Blauanteile berechnen
		R = int(0.5+(Feuchtigkeit-minF)*(colB[0]-colA[0])/(maxF-minF)+colA[0])
		G = int(0.5+(Feuchtigkeit-minF)*(colB[1]-colA[1])/(maxF-minF)+colA[1])
		B = int(0.5+(Feuchtigkeit-minF)*(colB[2]-colA[2])/(maxF-minF)+colA[2])
		X = [R,G,B]
	return X

if __name__ = "__main__":
	#j = 1
	while True:
		Datum = time.strftime("%y-%m-%d-%H")                             # Datum mit Stunde feststellen
		LuftfeuchtigkeitMessen("/home/pi/StartupProject/Feuchtigkeitsdaten_%s" % (Datum))
		AnzeigeMatrix = MesswerteNormieren()
		sensor.set_pixels(AnzeigeMatrix)	
		time.sleep(30)				                                  # 30 Sekunden warten
		#j += 1
		#if j > 5 :
		#	sensor.clear()
		#	break		                                              # While-Scheife unbedingt verlassen
		
		
	

