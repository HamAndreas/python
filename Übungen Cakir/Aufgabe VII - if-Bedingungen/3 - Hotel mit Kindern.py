# Schreiben Sie ein Programm, das für eine Familie d.h. zwei Erwachsene und ein Kind ein Angebot erstellt. Kinder 0 bis 6 Jahren übernachten kostenlos, ab 7 Jahren gibt es einen Rabatt von 70% auf den Zimmerpreis pro Person und Nacht
#
# Folgende Arbeitsschritte sind nötig: Wenn Alter des Kindes kleiner 7, dann beträgt der Rabatt 100%
# Sonst beträgt der Rabatt 70%
# Kinderpreis= Zimmerpreis x Aufenthaltsdauer x (1-Rabatt/100)

# Die Berechnung des Kinderpreises ist immer gleich, jedoch wird vorher der Rabatt abhängig vom Alter des Kindes gesetzt. Die Anweisung zum Setzen des Rabatts auf 100% wird nur dann ausgeführt, wenn das Alter des Kindes weniger als 7 Jahre beträgt. In allen anderen Fällen also Kinder ab 7 wird der Rabatt auf 70% gesetzt. (Tipp: Hier if else verwenden)