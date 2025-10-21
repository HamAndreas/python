# 	Aufgabe: Altersumrechnung
#		Erstellen Sie ein Programm, das das Alter eines Benutzers in Jahren von der Konsole einliest und dieses in Monaten umrechnet.
#	Anforderungen
#		○ Fragen Sie den Benutzer nach seinem Alter in Jahren
#		○ Konvertieren Sie den eingegebenen Wert von String zu int
#		○ Berechnen Sie das Alter in Monaten (1 Jahr = 12 Monate)
	
# Geben Sie das umgerechnete Alter in Monaten in der Konsole aus

user_alter=input(f"Wie alt sind Sie in Jahren? ")
user_alter_konv=int(user_alter)

user_alter_monate=user_alter_konv*12

print(f"Sie sind damit {user_alter_monate} Monate alt.")