# Anzahl der Ziffern einer Zahl zählen
# Beschreibung
# Schreiben Sie ein Programm, das den Benutzer auffordert, eine positive ganze Zahl einzugeben.
# Das Programm zählt die Anzahl der Ziffern in der Zahl und gibt das Ergebnis aus.

zahl=int()
anzahl=int()

print("Herzlich Willkommen beim Zahlen-Ziffern-Zähler in dem Sie eine Zahl eintragen und ich Ihnen die Anzahl der Ziffern mitteile.")
zahl=int(input("Bitte geben Sie eine positive ganze Zahl ein: "))

if zahl<=0:
    print("Die Zahl muss positiv sein.")
else:
    anzahl=0
    while zahl>0:
        zahl=zahl//10
        anzahl+=1
    print(f"Die Zahl hat {anzahl} Ziffern.")

print(f"Danke für's Mitmachen!")


