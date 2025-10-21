# Währungsumrechner
#	• Aufgabe: Schreibe ein Programm, das einen Betrag in Euro eingibt und diesen in US-Dollar umrechnet. Der Umrechnungskurs ist 1 Euro = 1,1 US-Dollar.
#	• Eingabe: Betrag in Euro.
# Ausgabe: Betrag in US-Dollar.

umrechnungskurs=1.1
betrag_euro=input("Bitte geben Sie den Wert in Euro an: ")
betrag_dollar=float(betrag_euro)*umrechnungskurs

print(f"{betrag_euro} Euro entsprechen {betrag_dollar:.2f} in USD.")