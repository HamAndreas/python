anzahl_personen=input(f"Wie viele Personen benötigen eine Übernachtung?")
anzahl_uebernachtungen=input(f"wie lange bleiben die {anzahl_personen} Personen?")
zimmerpreis=70
nettopreis=zimmerpreis*int(anzahl_uebernachtungen)*int(anzahl_personen)
gesamtpreis=nettopreis*1,19

print(f"Der Gesamtpreis beträgt für alle Personen {gesamtpreis} €")