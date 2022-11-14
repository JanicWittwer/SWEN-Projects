# Projektarbeit SWEN (Softwareentwicklung)


## Ausgangslage und Projektidee

Im Freundeskreis haben wir ein Würfelspiel, welches wir gerne spielen. Gerne möchten wir dieses Würfelspiel nun in Python programmieren.

### Spielidee 

Beim Spiel handelt es sich um ein klassisches Würfelspiel, welches auf Glück und auf Wahrscheinlichkeiten beruht. Es geht darum, in den richtigen Momenten weiter zu spielen oder in den richtigen Momenten die Punkte ausfzuschreiben und das Glück auf seiner Seite zu haben. Das Spiel hat verschiedene Regeln, welche wir im folgenden nun kurz beschreiben möchten.

Anzahl Spieler: 1-6
Maximale Punktzahl zum erreichen: 10000
Anzahl Würfel: 6
Spieldauer: unbegrenzt, bis 10000 Punkte erreicht sind


### Ablauf:

Eine Runde von max. 6 Spielern muss mit dem Werfen von Würfeln möglichst schnell möglichst viele Punkte sammeln. Die Würfel geben dabei je nach Wurf und je nach Kombination mehr oder weniger Punkte.

Der erste Spieler würfelt mit allen 6 Würfeln. Je nach Wurf gibt es verschiedene Anzahl von Punkte, zudem darf nur mit bestimmten Würfeln auch «weitergewürfelt» werden.

Punktzahlen

Jede "1" = 100 Punkte

Jede "5" = 50 Punkte 

Dreierkombi mit "1" = 1000 Punkte   (Würfelwurf enthält die Würfel 1,1,1)

Dreierkombi mit "2" = 200 Punkte    (Würfelwurf enthält die Würfel 2,2,2)

Dreierkombi mit "3" = 300 Punkte    (Würfelwurf enthält die Würfel 3,3,3)

Dreierkombi mit "4" = 400 Punkte    (Würfelwurf enthält die Würfel 4,4,4)

Dreierkombi mit "5" = 500 Punkte    (Würfelwurf enthält die Würfel 5,5,5)

Dreierkombi mit "6" = 600 Punkte    (Würfelwurf enthält die Würfel 6,6,6)

Treppe aus 3 Paaren = 750 Punkte    (Bsp. Würfel 1,1 , 2,2, und 5,5)

Strasse             = 1500 Punkte   (Würfelwurf mit 1,2,3,4,5,6)


Sofern ich eine 1 oder 5 habe, kann ich die entsprechenden Würfel rausnehmen und mit den übrig bleibenden Würfeln weiterwürfeln. Bsp. Ich würfle im ersten Wurf (1, 5, 4, 6, 6, 2), daraus kann ich die 1 rausnehmen. Gibt 100 Punkte. Entweder kann ich diese Punkte nun aufschreiben oder weiterspielen mit den restlichen 5 Würfeln. Ich würfle weiter und werfe im zweiten Wurf (4, 2, 6, 1, 1). Davon nehme ich die beiden 1 raus und habe noch 3 Würfel zur Verfügung. Ich habe wieder die Entscheidung ob ich nun die 300 Punkte aufschreiben möchte oder mit den anderen 3 Würfeln noch weiterwürfeln möchte. Ich schreibe auf und habe nun 300 Punkte gesammelt und der nächste Spieler ist an der Reihe. Falls ich in der soeben genannten Situation anders entschieden hätte und weitergespielt hätte, gehe ich ein gewisses Risiko ein. Ich kann so zwar mehr Punkte sammeln, da ich nochmals würfel kann und meine Summe an Punkten damit erhöhen kann. Falls ich aber keine 1, 5 oder eine andere oben genannte Kombination würfle, verliere ich die in dieser Runde gesammelten Punkte und ich kann meine Totalpunkte nicht vergrössern. Wenn ich alle 6 Würfel geworfen habe und ich auch überall etwas schreiben konnte (dabei bei keinem Wurf keine Punkte geholt habe), kann ich mit allen 6 Würfeln wieder neu beginnen zu würfen. Dies ist wahrscheinlich die beste Situation, da ich so sofort wieder eine hohe Chance auf viele Punkte habe.

Derjenige Spieler, welcher zuerst 10'000 Punkte erreicht hat, gewinnt das Spiel



## Vorgehensweise

Die Aufgabe erfordert die Umsetzung von verschiedenen Schritten, damit dieses Würfelspiel auf Python umgesetzt werden kann. Dazu haben wir eine Reihe von verschiedenen Tasks zusammengestellt, welche wir systematisch und Schrittweise lösen möchten. Als Bonus sollen die verschiedenen Schritte schlussendlich zusammengefügt werden.

Verschiedene Tasks, welche wir zusammengestellt haben
- Bei Spielbeginn kann die Anzahl Mitspieler angegeben werden
- Der Spieler kann würfeln
- Der Spieler  kann einen Entscheidung eingeben, welche Würfel er wählen möchte
- Der Spieler kann entscheiden, ob er weiterspielen möchte.
- Es wird ein Punktetotal aufgrund der Würfelwahl berechnet
- Das Punktetotal wird dem "Spiel-Konto" des Spielers gutgeschrieben
- Spieler erreicht 10'000 Punkte und gewinnt
