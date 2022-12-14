
# Imports

import random

# Definition von unseren zentralen Funktionen für das Spiel

## Funktion Spielereingabe
def spieler_eingabe():
    while True:
        anzahl_spieler = input("Bitte Anzahl Spieler eingeben: ___")    
        if anzahl_spieler >= "2" and anzahl_spieler <= "6" :
            return int(anzahl_spieler)
        else:
            print("Die Anzahl Spieler muss zwischen 2 und 6 liegen")

## Funktion Würfelwurf
def wuerfeln(anzahlwuerfel = 6):
    janein = input("Möchtest du die Würfel würfeln? j/n \n")
    if janein == "j":
        print("Dann lass uns beginnen!")
        
        wuerfelliste = [random.randint(1, 6) for i in range(anzahlwuerfel)]
        print(wuerfelliste)
        return wuerfelliste

    if janein == "n": #(Diese Funktion ist aktuell nicht umgesetzt)
        spielerwechsel()



## Funktion Punktevalidierung
def hat_punkte(wuerfelliste):
    hat_punkte = False
    
    anzahl_eins = wuerfelliste.count(1)
    anzahl_zwei = wuerfelliste.count(2)
    anzahl_drei = wuerfelliste.count(3)
    anzahl_vier = wuerfelliste.count(4)
    anzahl_fuenf = wuerfelliste.count(5)
    anzahl_sechs = wuerfelliste.count(6)

    kombinationen = [anzahl_eins, anzahl_zwei, anzahl_drei, anzahl_vier, anzahl_fuenf, anzahl_sechs]
    
    if 1 in wuerfelliste:
        print("Super, du hast eine 1 gewürfelt, das gibt Punkte")
        hat_punkte = True

    if 5 in wuerfelliste:
        print("Super, du hast eine 5 gewürfelt, das gibt Punkte")
        hat_punkte = True

    for index,anzahl in enumerate(kombinationen):
        if anzahl >= 3:
            print(f"Super, du hast eine Dreierkombination von {index+1} gewürfelt, das gibt Punkte")
            hat_punkte = True

    if not hat_punkte:
        print("Leider hast du keine Punkte gewürfelt")
    

    else:
        print("Gratuliere, du hast Punkte erreicht...")

    return hat_punkte


## Funktion Würfelauswahl
def auswahl(wuerfelliste):
    wuerfel_raus = []
    nochmals = ("j")
    while nochmals == "j":
        was_entfernen = int(input("Welche Würfel willst du rausnehmen?\n"))
        wuerfelliste.remove(was_entfernen)
        wuerfel_raus.append(was_entfernen)
        nochmals = input("Willst du weitere Würfel rausnehmen? j/n \n")
    return wuerfel_raus



## Funktion Punkte aufschreiben
def punkte(wuerfel_raus):
    zwischenpunktestand = 0
    
    for wurf in range(1,7):
        if wuerfel_raus.count(wurf) >= 3:
            if wurf == 1:
                zwischenpunktestand += 1000
            else:
                zwischenpunktestand += wurf *100
        elif wuerfel_raus.count(wurf) >= 1:
            if wurf == 1:
                zwischenpunktestand += 100 * wuerfel_raus.count(wurf)
            if wurf == 5:
                zwischenpunktestand += 50 * wuerfel_raus.count(wurf)

    return zwischenpunktestand


## Hier erstellen wir die verschiedenen Spieler-Konten (aktuell nicht verwendet in der Spiel-Simulation)
## Würde benötigt werden um die generierten Punkte pro Spielrunden den verschiedenen Spielern gutzuschreiben.
class Spieler:
    def __init__(self, name):
        self.name = name
        self.punktestand_temp = 0
        self.punktestand_total = 0

    

## Funktion Gesamt-Spiel-Simulation
def main():
    print("\n")
    print("******** Herzlich willkommen zu Fraggles ********")
    print("\n")
    print("Bei Fraggles handelt es sich um ein Würfelspiel für Gross und Klein.")
    print("Entscheide Dich im richtigen Moment fürs Risiko oder für die sichere Variante.")
    print("Aber Achtung! --> Dieses Würfelspiel bietet Sucht- und auch ein erhebliches Frustrations-Potenzial! ;-D ")
    print("\n")
    print("Das Spiel eignet sich von 2 bis 6 Spieler")
    print("\n")

    anzahl_spieler = spieler_eingabe()

    print("\n")
    print("Super, es werden in dieser Runde " + str(anzahl_spieler) + " Spieler mitmachen.")
    print("\n")
    print("Als nächstes kannst du die Namen von allen Spielern eingeben.")
    print("\n")


    spieler = []

    for i in range(anzahl_spieler):
        neuer_spieler = Spieler(input(f"Bitte gib den Namen von Spieler {i+1} ein: "))
        spieler.append(neuer_spieler)

    print("\n")
    print("Sehr schön - jetzt wird gewürfelt!")
    print("\n")

    wuerfelliste = wuerfeln()

    # Wenn ich Punkte gemacht haben, dann können wir nun unsere Würfel auswählen.
    # Das wiederholt sich nun, bis alle Würfel rausgenommen wurden.
    if hat_punkte(wuerfelliste) == True:
        zwischenstand = auswahl(wuerfelliste)
        print(f"Folgende Würfel hast du bereits herausgenommen " + str(zwischenstand))
        print(f"Die folgenden Würfel hast du noch zur Auswahl " + str(wuerfelliste))

        zwischenstand = punkte(zwischenstand)
        print(f"Du schreibst nun die folgenden Punkte auf: " + str(zwischenstand))

    # Wenn wir keine Punkte gemacht haben, dann kommt der nächste Spieler an die Reihe
    # (Diese Funktion ist aktuell noch nicht umgesetzt)  
    # else:
        # spielerwechsel()

    # Wir wollen erneut würfeln
    wuerfelliste = wuerfeln(len(wuerfelliste))



# Ausführung Spielsimulation mit Main
if __name__ == "__main__":
    main()

