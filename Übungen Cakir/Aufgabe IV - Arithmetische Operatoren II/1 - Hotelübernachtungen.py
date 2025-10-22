# Der Projektleiter beauftragt Sie, ein Programm zu entwickeln, das ein Angebot für Hotelübernachtungen erstellen soll. (Datenkonvertierung)
# Die Analyse ergibt folgende Schritte: 
# Eingabe von 
#	○ Anzahl der Personen
#	○ Aufenthaltsdauer
# Der Gesamtpreis wird wie folgt berechnet, wobei der Zimmerpreis 70 Euro pro Person und Nacht beträgt
#	○ Nettopreis = Zimmerpreis x Aufenthaltsdauer x Anzahl der Personen
#	○ Gesamtpreis = Mehrwertsteuer zusätzlich 
# Bildschirm soll Gesamtpreis ausgegeben werden 
#		Info: Um das Programm zu entwerfen und zu implementieren, sind folgende Sprachelemente notwendig:  
#		i. Variablen
#		ii. Eingabe und Ausgabe
#		iii. Arithmetische Operationen

anzahl_personen=input(f"Wie viele Personen benötigen eine Übernachtung? ")
anzahl_uebernachtungen=input(f"wie lange bleiben die {anzahl_personen} Personen? ")
zimmerpreis=70
nettopreis=zimmerpreis*float(anzahl_uebernachtungen)*float(anzahl_personen)
gesamtpreis=nettopreis*1.19

print(f"Der Gesamtpreis für alle Personen beträgt {gesamtpreis} €")