zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

print("Was möchtest du tun?")
print("1:Addieren")
print("2:Subtrahieren")
print("3:Multiplizieren")
print("4:Dividieren")

operation = input("Wähle eine Rechnung: ")

if (operation == "1"):
    ergebnis = zahl1 + zahl2
    print(f"Das Ergebnis der Addition von {zahl1} und {zahl2} lautet {ergebnis}.")
elif (operation == "2"):
    ergebnis = zahl1 - zahl2
    print(f"Das Ergebnis der Subtraktion von {zahl1} und {zahl2} lautet {ergebnis}.")
elif (operation == "3"):
    ergebnis = zahl1 * zahl2
    print(f"Das Ergebnis der Multiplikation von {zahl1} und {zahl2} lautet {ergebnis}.")
elif (operation == "4"):
    ergebnis = zahl1 / zahl2
    if (zahl2 != 0):
        print(f"Das Ergebnis der Division von {zahl1} und {zahl2} lautet {ergebnis}.")
    else: 
        print("Fehler: Deine Zahl darf nicht Null sein")
else:
    print("Ungültige Eingabe")