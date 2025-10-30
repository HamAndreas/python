#Aufgabe 1: Deklaration mehrerer Variablen
name = str("Andreas")
alter = int(38)
hoehe = float(1.80)

print(f"Name: {name} Alter: {alter} Größe:  {hoehe}m")

# Aufgabe 2: Berechnung und Zuweisung
a = float(5.6)
b = float(3.2)
c = float(1.8)

print(f"Die Fläche eines Rechtecks mit den Seitenlängen {a}m und {b}m beträgt {a*b}m²")

# Aufgabe 3: Deklariere und initialisiere
alter3 = int(42)
temp3 = float(38.6)
name3 = str("Pixel")
esregnet3 = bool(False)

print(f"Ich bin {alter3} Jahre alt und habe eine Körpertemperatur von {temp3}°C. Ich habe ein Haustier names {name3}. Die Antwort auf die Frage, Regnet es draußen, lautet: {esregnet3}")

# Aufgabe 4: Deklariere und initialisiere
a = int(7)
b = int(3)
radius = float(32)
kreis_flaeche = float(3.14 * radius**2)
text1 = str(f"Die Fläche eines Kreises")
text2 = str(f" mit dem Radius {radius}cm beträgt {kreis_flaeche}cm²")
nachricht = str(text1+text2)
print(nachricht)

# Aufgabe 5: Benutzereingaben speichern
name5 = input("Wie lautet dein Name? ")
alter5 = input("Wie alt bist du? ")
essen5 = input("Was isst du am liebsten? ")
print(f"Hallo {name5}, schön dich mit {alter5} noch so quietschfidel zu sehen. Da dein Lieblingsessen {essen5} ist, scheinst du ein echter Feinschmecker zu sein.")
