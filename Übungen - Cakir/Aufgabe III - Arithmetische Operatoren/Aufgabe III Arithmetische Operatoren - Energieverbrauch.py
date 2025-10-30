tv_zeit = input("Wie lange schauen Sie täglich fern (in Stunden)? ")
tv_anzahl = input("Wie viele Fernseher gibt es im Haus? ")
stromverbrauch_tv = 1 #kWh pro Stunde
kochen_anzahl = input("Wie oft kochen Sie in der Woche? ")
kochen_stunden = input("Wie lange kochen Sie dabei im Schnitt in Stunden? ")
stromverbrauch_herd = 2 #kWh pro Stunde
internet_nutzung = input("Wie lange nutzen Sie das Internet am Tag? ")
stromverbrauch_internet = 2 #kWh pro Stunde
heizung = input("An wie vielen Tagen im Jahr heizen Sie? ")
stromverbrauch_heizung = 8 #kWh pro Stunde
strompreis = input("Wie hoch ist der Strompreis bei ihrem aktuellen Stomanbieter pro kWh in Euro? ")

stromverbrauch_jahr = (float(tv_zeit) * float(tv_anzahl) * stromverbrauch_tv + float(kochen_anzahl) * float(kochen_stunden) * stromverbrauch_herd + float(internet_nutzung) * stromverbrauch_internet + float(heizung) * stromverbrauch_heizung) * 365
kosten_jahr = stromverbrauch_jahr * float(strompreis)

print(f"Der jährliche Stromverbrauch beträgt {stromverbrauch_jahr:,.2f} kWh und die jährlichen Stromkosten belaufen sich auf {round(kosten_jahr, 2)} Euro.")

