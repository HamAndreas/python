# Schreiben Sie ein Programm, das einen Aufschlag z.B. 20 Euro berechnet, wenn der Gast nur einen Tag im Hotel übernachtet. 
# Die Analyse des Arbeitsauftrages ergibt folgende wesentliche Verarbeitungsschritte
#	Nettobetrag = Zimmerpreis x Aufenthaltsdauer x Anzahl der Personen
#	Wenn Aufenthaltsdauer = 1, dann addiere 20 Euro zu Nettobetrag
#	
# Info: Der erste Berechnungsschritt wird immer ausgeführt. Der zweite Berechnungsschritt soll nur dann ausgeführt werden, wenn die Bedingung "Aufenthaltsdauer = 1 Tag" zutrifft. 
# 
# Variablen: Zimmerpreis =70;
# Anzahl der Personen, Aufenthaltsdauer
# Mwst
# Gesamtpreis;
# Nettopreis;
# EingabeAufenthaltsdauer;
# EingabeAnzahlderPerson;

zimmerpreis=float(70)
anzahl_personen=int()
aufenthalt=int()
mwst=float(19.0)
gesamtpreis=float()
nettopreis=float()
aufschlag=float(20)

print(f"Herzlich Willkommen zum absolut realitätsnahen Hotelübernachtungskosten-Berechnungstool. Der aktuelle Zimmerpreis beträgt {zimmerpreis} Euro.")
anzahl_personen=int(input("Bitte geben Sie die Anzahl der Personen an, die eine Übernachtung benötigen: "))
aufenthalt=int(input("Bitte geben Sie die Anzahl der Übernachtungen an, die Sie gerne bleiben möchten: "))
if aufenthalt==1:
    print(f"Frechheit, dass Sie nur eine Nacht bleiben wollen. Dafür berechnen wir Ihnen {aufschlag} Euro zusätzlich.")
    nettopreis=zimmerpreis*anzahl_personen*aufenthalt+aufschlag
    gesamtpreis=nettopreis*(1+mwst/100)
else:
    nettopreis=zimmerpreis*anzahl_personen*aufenthalt
    gesamtpreis=nettopreis*(1+mwst/100)

print(f"Der Gesamtpreis für {aufenthalt} Übernachtungen mit {anzahl_personen} Personen beträgt {gesamtpreis:.2f} Euro.")


