# Aufgabe 1: Anwendung "Zinsberechnung" erstellen
startkapital = float(input("Wieviel Geld haben Sie gerade zur Verfügung um es anzulegen? "))
zinssatz = float(input("Wie hoch ist der Zinssatz ihrer Anlageform in Prozent? "))
print(f"Nach einem Jahr wird aus Ihrem Startkapital von {startkapital} € eine stattliche Summe von {round(startkapital * (1 + zinssatz / 100), 2)} € geworden sein. Das sind immerhin satte {round(startkapital * (1+ zinssatz / 100) - startkapital, 2)} € an Zinsen!")
