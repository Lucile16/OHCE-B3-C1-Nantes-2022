import unittest
# Pour réussir lancer le test, il faut taper cette commande : "py -m test.ohce_test" dans le répertoire OHCE (dans un terminal)
from src.ohce import ohce

class OhceTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        # Quand on saisit une chaîne
        o = ohce()
        chaine = input("Entrez un mot : ")
        resultat = o.palindrome(chaine)
        # Alors celle-ci est renvoyée en miroir
        return self.assertEqual("tset", resultat)

if __name__ == '__main__':
    unittest.main()