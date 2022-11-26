# Das ist unsere Hauptdatei für die Projektarbeit

## Teil 1: Anzahl Spieler und Spielernamen
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

    

## Teil 2: Würfeln-Funktion mit 6 Würfeln
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

            
    
## Interpretation des Würfelwurfs anhand der Werte/Regeln
### Als nächstes möchten wir prüfen, ob der Würfelwurf Werte enthält, welche auch tatsächlich Punkte ergeben. Dazu haben wir verschiedene Regeln programmiert, welche von unserem Programm geprüft werden.   
### Die Würfelfunktion aus Teil 2 wurde hier ebenfalls mitgenommen.    

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

            
            wuerfelliste = [str(wuerfel1), str(wuerfel2), str(wuerfel3), str(wuerfel4), str(wuerfel5), str(wuerfel6)]
            print(wuerfelliste)
            anzahl_eins = wuerfelliste.count(str(1))
            anzahl_zwei = wuerfelliste.count(str(2))
            anzahl_drei = wuerfelliste.count(str(3))
            anzahl_vier = wuerfelliste.count(str(4))
            anzahl_fuenf = wuerfelliste.count(str(5))
            anzahl_sechs = wuerfelliste.count(str(6))

            kombinationen = [anzahl_eins, anzahl_zwei, anzahl_drei, anzahl_vier, anzahl_fuenf, anzahl_sechs]

            strasse = [str(1),str(2), str(3), str(4), str(5), str(6)]

            for i in wuerfelliste:
                if str(1) in i:
                    print("Super, du hast eine 1 gewürfelt, das gibt Punkte")
                
                elif str(5) in i:
                    print("Super, du hast eine 5 gewürfelt, das gibt Punkte")
                
            for i in kombinationen:
                if i >= 3:
                    print("Super, du hast eine Dreierkombination gewürfelt, das gibt Punkte")

            if wuerfelliste == strasse:
                print("Super, du hast eine Strasse gewürfelt, das gibt Punkte")


        elif janein == "n":
            print ("Okay, dann schreiben wir deine Punkte auf...")
            quit()
            
            
