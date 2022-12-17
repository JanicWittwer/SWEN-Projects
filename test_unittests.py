
import unittest
from Wuerfelspiel_Fraggles import spieler_eingabe

class Test1(unittest.TestCase):
    def test_1(self):
        self.assertTrue(spieler_eingabe)

#assertEqual --> Um ein erwartetes Ergebnis zu prüfen.
#assertTrue --> Um eine Bedingung zu verifizieren.
#assertFalse --> Um eine Bedingung zu verifizieren.
#assertRises --> Um zu prüfen, ob eine bestimmte Ausnahme ausgelöst wird.

if __name__ == '__main__':
    unittest.main()
