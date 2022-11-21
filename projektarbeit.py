# Das ist unsere Hauptdatei für die Projektarbeit

## Würfeln-Funktion mit 6 Würfeln
### Erste Funktion, welche wir umgesetzt haben. Hier programmieren wir , dass ein einzelner Spieler die Funktion hat, mit 6 Würfeln immer wieder zu würfeln. Mittel Ja und Nein Input-Befehlen kann er sagen, ob er erneut würfeln möchte. Es sind noch keine Anzahl Spieler, keine Punkte, keine Regelen und keine Spiellogik implementiert.


import random
import time

Playing = True

while Playing:
    while True:

        janein = input("Möchtest du die Würfel würfeln? j/n\n>")
        if janein == "j":
            print("Dann lass uns beginnen!")
            wuerfel1 = random.randint(1, 6)
            wuerfel2 = random.randint(1, 6)
            wuerfel3 = random.randint(1, 6)
            wuerfel4 = random.randint(1, 6)
            wuerfel5 = random.randint(1, 6)
            wuerfel6 = random.randint(1, 6)
            print("Der Würfel zeigt: " + str(wuerfel1))
            print("Der Würfel zeigt: " + str(wuerfel2))
            print("Der Würfel zeigt: " + str(wuerfel3))
            print("Der Würfel zeigt: " + str(wuerfel4))
            print("Der Würfel zeigt: " + str(wuerfel5))
            print("Der Würfel zeigt: " + str(wuerfel6))
        elif janein == "n":
            print ("Okay, dann schreiben wir deine Punkte auf...")
            quit()

            
## Anzahl Spieler und Spielernamen
### Wir möchten nun eine Funktion einbauen, wo am Anfang eine Anzahl Spieler gewählt werden kann und auch Spielernamen eingegeben werden können.


print("Herzlich willkommen zu Fraggles - Das würfligste Würfelspiel für Gross und Klein. Bei diesem Spiel gehen Freundschaften zu Bruch.")

def spieler_eingabe():
    while True:
        anzahl_spieler = input("Bitte Anzahl Spieler eingeben: ")    
        if anzahl_spieler >= "2" and anzahl_spieler <= "6" :
            return int(anzahl_spieler)
        else:
            print("Die Anzahl Spieler muss zwischen 2 und 6 liegen")

anzahl_spieler = spieler_eingabe()
print(anzahl_spieler)


class Spieler:
    def __init__(self, name):
        self.name = name
        self.punktestand_temp = 0
        self.punktestand_total = 0

spieler = []

for i in range(anzahl_spieler):
    neuer_spieler = Spieler(input(f"Bitte gib den Namen von Spieler {i+1} ein: "))
    spieler.append(neuer_spieler)

