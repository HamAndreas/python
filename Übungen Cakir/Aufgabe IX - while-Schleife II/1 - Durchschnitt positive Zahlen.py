# Benutzer gibt positive Zahlen ein und berechnet den Durchschnitt
# Beschreibung
# Schreiben Sie ein Programm, das den Benutzer auffordert, positive Zahlen einzugeben. 
# Das Programm berechnet den Durchschnitt der eingegebenen Zahlen, bis der Benutzer eine negative Zahl eingibt.


user_input=int(0)                                                       # Variable für Nutzereingabe definieren
summe=int()                                                             # Variable für die Summe (aller Eingaben) definieren
anzahl_eingaben=int(1)                                                  # Variable für die Anzahl an Eingaben des Nutzers
durchschnitt=float(0)                                                   # Variable für den Durchschnitt (float)

user_input=int(input("Bitte geben Sie eine Zahl ein, um den Durchschnitt aller eingetragenen Zahlen zu errechnen: "))

while user_input>=0:                                                    # solange die eingegebene Zahl nicht negativ ist, wird die while-Schleife ausgeführt
    summe+=user_input                                                   # Summe um Nutzereingabe erhöhen
    durchschnitt=summe/anzahl_eingaben                                  # Durchschnitt aus Summe und der Einzahl an Eingaben berechnen
    print(f"Der Durchschnitt liegt bei {durchschnitt:.2f}")             # Ausgabe des Durchschnitts
    print("-----------------------------------------------")            
    user_input=int(input("Bitte geben Sie eine weitere Zahl ein: "))    # Eingabeaufforderung für weitere Zahl
    anzahl_eingaben+=1                                                  # Anzahl der Eingaben wird um 1 erhöht

print("Da Sie eine negative Zahl eingegeben haben, wurde das Programm zur Sicherheit beendet.")