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


        elif janein == "n":
            print ("Okay, dann schreiben wir deine Punkte auf...")
            quit()
            

            
            
            
#Kombinierte Version
###(Entwurf, aber schon einiges reinkopiert)


#Imports

import random
import time

# Definition von unseren zentralen Funktionen für das Spiel

def spieler_eingabe():
    while True:
        anzahl_spieler = input("Bitte Anzahl Spieler eingeben: ___")    
        if anzahl_spieler >= "2" and anzahl_spieler <= "6" :
            return int(anzahl_spieler)
        else:
            print("Die Anzahl Spieler muss zwischen 2 und 6 liegen")


# Nun definieren wir unsere Standard-Würfelfunktion für 6 Würfel

def wuerfeln():
    janein = input("Möchtest du die Würfel würfeln? j/n\n>")
    if janein == "j":
        print("Dann lass uns beginnen!")
        wuerfel1 = random.randint(1, 6)
        wuerfel2 = random.randint(1, 6)
        wuerfel3 = random.randint(1, 6)
        wuerfel4 = random.randint(1, 6)
        wuerfel5 = random.randint(1, 6)
        wuerfel6 = random.randint(1, 6)
        print(f"Der Würfel zeigt: {wuerfel1}")
        print(f"Der Würfel zeigt: {wuerfel2}")
        print(f"Der Würfel zeigt: {wuerfel3}")
        print(f"Der Würfel zeigt: {wuerfel4}")
        print(f"Der Würfel zeigt: {wuerfel5}")
        print(f"Der Würfel zeigt: {wuerfel6}")

        wuerfelliste = [wuerfel1, wuerfel2, wuerfel3, wuerfel4, wuerfel5, wuerfel6]
        print(wuerfelliste)
        return wuerfelliste



def hatpunkte(wuerfelliste):
    hatpunkte = False
    
    anzahl_eins = wuerfelliste.count(1)
    anzahl_zwei = wuerfelliste.count(2)
    anzahl_drei = wuerfelliste.count(3)
    anzahl_vier = wuerfelliste.count(4)
    anzahl_fuenf = wuerfelliste.count(5)
    anzahl_sechs = wuerfelliste.count(6)

    kombinationen = [anzahl_eins, anzahl_zwei, anzahl_drei, anzahl_vier, anzahl_fuenf, anzahl_sechs]
    
    if 1 in wuerfelliste:
        print("Super, du hast eine 1 gewürfelt, das gibt Punkte")
        hatpunkte = True

    if 5 in wuerfelliste:
        print("Super, du hast eine 5 gewürfelt, das gibt Punkte")
        hatpunkte = True

    for index,anzahl in enumerate(kombinationen):
        if anzahl >= 3:
            print(f"Super, du hast eine Dreierkombination von {index+1} gewürfelt, das gibt Punkte")
            hatpunkte = True

    if not hatpunkte:
        print("Leider hast du keine Punkte gewürfelt")
    

    else:
        print("Gratuliere, du hast Punkte erreicht...")

    return hatpunkte


#Entwurf der Auswahl-Funktion der Würfel

def auswahl(wuerfelliste):
    wuerfelraus = []
    was_entfernen = int(input("Welche Würfel willst du rausnehmen "))
    wuerfelliste.remove(was_entfernen)
    wuerfelraus.append(was_entfernen)
    return wuerfelraus

zwischenstand = auswahl(wuerfelliste)

print(zwischenstand)
print(wuerfelliste)



def spielerwechsel():
    pass #irgendwie müssen wir es schaffen, dass sich hier die Klasse ändert


#def punkteermitteln
#for i in wuerfelliste:
    #if i == 1: return(100)

# SPIEL

print("\n")
print("******** Herzlich willkommen zu Fraggles ********")
print("\n")
print("Bei Fraggles handelt es sich um ein Würfelspiel für Gross und Klein. Entscheide Dich im richtigen Moment fürs Risiko oder für die sichere Variante. ")
print("Aber Achtung! --> Dieses Würfelspiel bietet Sucht- und auch ein erhebliches Frustrations-Potenzial! ;-D ")
print("\n")
print("Das Spiel eignet sich von 2 bis 6 Spieler")
print("\n")

#Funktion der Anzahl Spieler wird hier ausgeführt
anzahl_spieler = spieler_eingabe()

print("\n")
print("Super, es werden in dieser Runde " + str(anzahl_spieler) + " Spieler mitmachen.")
print("\n")
print("Als nächstes kannst du die Namen von allen Spielern eingeben.")
print("\n")

#Hier erstellen wir die verschiedenen Speiler-Konten
class Spieler:
    def __init__(self, name):
        self.name = name
        self.punktestand_temp = 0
        self.punktestand_total = 0

spieler = []

for i in range(anzahl_spieler):
    neuer_spieler = Spieler(input(f"Bitte gib den Namen von Spieler {i+1} ein: "))
    spieler.append(neuer_spieler)

print("\n>")
print("Sehr schön - jetzt wird gewürfelt!")
print("\n>")

wuerfelliste = wuerfeln()

#Wenn ich Punkte gemacht haben, dann können wir nun unsere Würfel auswählen.
if hatpunkte(wuerfelliste) == True:
    auswahl()

#Wenn wir keine Punkte gemacht haben, dann kommt der nächste Spieler an die Reihe
else:
    spielerwechsel()

#Weiterspielen



