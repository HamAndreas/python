# Deklariere und initialisiere Variablen, die die Menge und den Preis von verschiedenen Lebensmitteln speichern. Berechne den Gesamtpreis des Einkaufs und gib ihn in der Konsole aus.
# Anforderungen:
#   • Speichere die Anzahl von Äpfeln, Bananen und Orangen als int.
#   • Speichere die Preise pro Stück für Äpfel, Bananen und Orangen als double.
# Berechne den Gesamtpreis für jede Obstart und addiere die Preise, um den Gesamtbetrag des Einkaufs zu erhalten.

anzahl_äpfel=5
anzahl_bananen=2
anzahl_orangen=4

preis_apfel=0.3
preis_banane=0.45
preis_orange=0.6

gesamtpreis_äpfel=anzahl_äpfel*preis_apfel
gesamtpreis_bananen=anzahl_bananen*preis_banane
gesamtpreis_orangen=anzahl_orangen*preis_orange

gesamtpreis=gesamtpreis_äpfel+gesamtpreis_bananen+gesamtpreis_orangen

print(f"Der Gesamtpreis für den Einkauf von {anzahl_äpfel} Äpfeln, {anzahl_bananen} Bananen und {anzahl_orangen} Orangen beträgt {gesamtpreis} €.")