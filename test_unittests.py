
# Wir haben versucht, die Unittests für unsere Funktionen aufzubauen. Das dazu notwendige Testfile haben wir erstellt.
# Bei der Erstellung der Testparameter für unsere Funktionen sind wir aber leider gescheitert, obwohl wir viel Zeit investiert haben :-(

import unittest
from Wuerfelspiel_Fraggles import spieler_eingabe

class Test1(unittest.TestCase):
    def test_1(self):
        self.assertTrue(spieler_eingabe)

class Test2(unittest.TestCase):
    def test_2(self):
        self.assertEqual(4, 4)
        # Hier scheitern wir, eine sinnvolle Bedingung für unseren Test einzubauen
        
if __name__ == '__main__':
    unittest.main()

#assertEqual --> Testmethode, um ein erwartetes Ergebnis zu prüfen.
#assertTrue --> Testmethode, um eine Bedingung zu verifizieren.
#assertFalse --> Testmethode, um eine Bedingung zu verifizieren.
#assertRises --> Testmethode, um zu prüfen, ob eine bestimmte Ausnahme ausgelöst wird.
