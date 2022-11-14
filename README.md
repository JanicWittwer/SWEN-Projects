# SWEN-Projects

#Beschreibung der Aufgabenstellung


Im Kollegenkreis haben wir ein Würfelspiel, welches wir gerne spielen. Gerne möchten wir dieses Würfelspiel nun in Python programmieren

Das Spiel hat verschiedene Regeln, welche wir nun kurz beschreiben möchten.

Anzahl Spieler: 1-6
Maximale Punktzahl zum erreichen: 10000
Anzahl Würfel: 6
Spieldauer: unbegrenzt, bis 10000 Punkte erreicht sind

Ablauf:

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


Sofern ich eine 1 oder 5 habe, kann ich die entsprechenden Würfel rausnehmen und mit den übrig bleibenden Würfeln weiterwürfeln. Bsp. Ich würfle im ersten Wurf (1, 5, 4, 6, 6, 2), daraus kann ich die 1 rausnehmen. Gibt 100 Punkte. Entweder kann ich diese Punkte nun aufschreiben oder weiterspielen mit den restlichen 5 Würfeln. Ich würfle weiter und werfe im zweiten Wurf (4, 2, 6, 1, 1). Davon nehme ich die beiden 1 raus und habe noch 3 Würfel zur Verfügung. Ich habe wieder die Entscheidung ob ich nun die 300 Punkte aufschreiben möchte oder mit den anderen 3 Würfeln noch weiterwürfeln möchte. Ich schreibe auf und habe nun 300 Punkte gesammelt und der nächste Spieler ist an der Reihe. Es gibt noch einige zusätzliche Regeln, welche man auch noch implementieren könnte.


