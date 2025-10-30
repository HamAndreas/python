# Schreiben Sie ein Programm, das für eine Familie d.h. zwei Erwachsene und ein Kind ein Angebot erstellt. Kinder 0 bis 6 Jahren übernachten kostenlos, ab 7 Jahren gibt es einen Rabatt von 70% auf den Zimmerpreis pro Person und Nacht
#
# Folgende Arbeitsschritte sind nötig: Wenn Alter des Kindes kleiner 7, dann beträgt der Rabatt 100%
# Sonst beträgt der Rabatt 70%
# Kinderpreis= Zimmerpreis x Aufenthaltsdauer x (1-Rabatt/100)

# Die Berechnung des Kinderpreises ist immer gleich, jedoch wird vorher der Rabatt abhängig vom Alter des Kindes gesetzt. Die Anweisung zum Setzen des Rabatts auf 100% wird nur dann ausgeführt, wenn das Alter des Kindes weniger als 7 Jahre beträgt. In allen anderen Fällen also Kinder ab 7 wird der Rabatt auf 70% gesetzt. (Tipp: Hier if else verwenden)


anzahl_erwachsene=int(2)
anzahl_kinder=int(1)
alter_kind=int(0)
rabatt=int(70)
kinderpreis=float(0)
zimmerpreis=float(70)
aufenthalt=int(0)
erwachenenpreis=float(0)
gesamtpreis=float(0)

print(f"Herzlich Willkommen zum Hotel-Übernachtungskosten-Berechner Deluxe. Wir beherbergen nur zwei Erwachsene mit einem Kind.")
aufenthalt=float(input(f"Bitte geben Sie zunächst an, wie lange (in Tagen) Sie bleiben möchten: "))
alter_kind=float(input(f"Geben Sie nun das Alter Ihres Kindes an: "))

if alter_kind<=6:
    rabatt=100
else:
    rabatt=70

kinderpreis=aufenthalt*zimmerpreis*(1-rabatt/100)
erwachenenpreis=aufenthalt*anzahl_erwachsene*zimmerpreis
gesamtpreis=erwachenenpreis+kinderpreis

bestätigung=input(f"Vielen Dank für Ihre Eingabe. Der Gesamtpreis für Ihre Buchung beträgt {gesamtpreis:.2f} €. Bitte bestätigen Sie Ihre Buchung durch Eingabe von 'Jawoll'.")

if bestätigung=="Jawoll":
    print(f"Vielen Dank für Ihre Buchung!")
else:
    print("Buchung abgebrochen. Bis zum nächsten Mal.")
