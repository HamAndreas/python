# Eingabe der Zahlen
zahl1 = float(input("Bitte trage die erste Zahl ein: "))
zahl2 = float(input("Bitte trage die zweite Zahl ein: "))

# Rechenfunktionen
def addition(a, b):
    ergebnis = a + b
    print(f"Das Ergebnis der Addition von {a} und {b} ist {ergebnis}.")

def subtraktion(a, b):
    ergebnis = a - b
    print(f"Das Ergebnis der Subtraktion von {a} und {b} ist {ergebnis}.")

def multiplikation(a, b):
    ergebnis = a * b
    print(f"Das Ergebnis der Multiplikation von {a} und {b} ist {ergebnis}.")

def division(a, b):
    ergebnis = a / b
    print(f"Das Ergebnis der Division von {a} und {b} ist {ergebnis}.")

# Menü zur Auswahl der Operation
def operation_waehlen():
    print("Was möchtest du tun?")
    print("1: Addieren")
    print("2: Subtrahieren")
    print("3: Multiplizieren")
    print("4: Dividieren")

    operation = input("Wähle eine Rechnung: ")

    if operation == "1":
        addition(zahl1, zahl2)
    elif operation == "2":
        subtraktion(zahl1, zahl2)
    elif operation == "3":
        multiplikation(zahl1, zahl2)
    elif operation == "4":
        if zahl2 != 0:
            division(zahl1, zahl2)
        else:
            print("Fehler: Division durch 0 nicht erlaubt.")
            # neue Eingabe, falls durch 0 geteilt werden sollte
            neue_zahl1 = float(input("Bitte trage die erste Zahl ein: ")) 
            neue_zahl2 = float(input("Bitte trage die zweite Zahl ein: "))
            if neue_zahl2 != 0:
                division(neue_zahl1, neue_zahl2)
            else:
                print("Schon wieder 0 gewählt – Abbruch.")
    else:
        print("Ungültige Eingabe. Bitte nur 1, 2, 3 oder 4 eingeben.\n")
        operation_waehlen()  # nochmal fragen

# Start der Auswahl
operation_waehlen()
