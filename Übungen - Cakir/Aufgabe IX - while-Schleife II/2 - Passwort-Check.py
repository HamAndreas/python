# Einfache Passwortprüfung
# Beschreibung: 
# Schreiben Sie ein Programm, das den Benutzer auffordert, ein Passwort einzugeben.
# Der Benutzer hat maximal 3 Versuche, um das richtige Passwort (z.B. "passwort123") einzugeben.

passwort="passwort123"
user_input=str()
anzahl_versuche=int(0)

print("Herzlich Willkommen zum Passwort-Ratespiel.")

while anzahl_versuche<3:
    print(f"Noch {3-anzahl_versuche} Versuche übrig.")
    user_input=input("Wie lautet das Passwort? ")
    anzahl_versuche+=1
    if user_input==passwort:
        print(f"Herzlichen Glückwunsch, Sie haben das Passwort {passwort} erraten.")
        print("-----------------------------")
        break
    else:
        print(f"{user_input} ist leider nicht richtig.")
        print("-----------------------------")

print("\nDas war's. Danke fürs Mitmachen!")