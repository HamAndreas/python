# 	Aufgabe: Temperaturkonvertierung
#	Aufgabe: Erstellen Sie ein Programm, das eine Temperatur in Celsius von der Konsole einliest und diese in Fahrenheit umrechnet. 
#	Verwenden Sie die Formel:
#	Fahrenheit = (Celsius * 9/5)+32
#	Anforderungen
#		○ Fragen Sie den Benutzer nach einer Temperatur in Celsius
#		○ Konvertieren Sie den eingegebenen Wert von String zu int oder float
#		○ Berechnen Sie die Temperatur in Fahrenheit
#		○ Geben Sie die umgerechnete Temperatur in Fahrenheit in der Konsole aus

user_temp_celsius=input(f"Bitte geben Sie eine Temperatur in °C an: ")
temp_celsius=float(user_temp_celsius)

temp_fahrenheit=temp_celsius*9/5+32

print(f"Eine Temperatur von {user_temp_celsius} °C entspricht {temp_fahrenheit} °F.")