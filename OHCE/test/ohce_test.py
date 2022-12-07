import unittest
# Pour réussir lancer le test, il faut taper cette commande : "py -m test.ohce_test" dans le répertoire OHCE (dans un terminal)
from src.ohce import ohce
from src.constants import constants
import parameterized as parameterized

class OhceTest(unittest.TestCase):
    @parameterized.parameterized.expand(["toto", "test"])
    def testIsMirrored(self, mot):
        # QUAND on saisit un mot
        resultat = ohce().palindrome(mot)

        # ALORS celui-ci est renvoyé en miroir
        self.assertEqual(resultat, constants.Bonjour + mot[::-1])

    @parameterized.parameterized.expand(["kayak"])
    def testIsMirroredPalindrome(self, mot):
        # QUAND on saisit un mot
        resultat = ohce().palindrome(mot)

        # ALORS celui-ci est renvoyé ET «Bien dit» est envoyé ensuite
        self.assertEqual(resultat, constants.Bonjour + mot + constants.BienDit)

    def testGreetings(self):
        # QUAND on saisit un mot
        resultat = ohce().palindrome("")

        # ALORS «Bonjour» est envoyé avant toute réponse
        self.assertEqual(resultat, constants.Bonjour)
        
    def testLanguage(self):
        # QUAND on saisit un mot
        resultat = ohce().langue("En")

        # ALORS «Bonjour» est envoyé dans la langue correspondante
        self.assertEqual(resultat, constants.Hello)

# class OhceTest(unittest.TestCase):
#     def test_renvoi_miroir(self):
#         # Quand on saisit une chaîne
#         o = ohce()
#         chaine = input("Entrez un mot : ")
#         resultat = o.palindrome(chaine)
#         # Alors celle-ci est renvoyée en miroir
#         self.assertEqual("radar", resultat)
#     def test_palindrome(self):
#         # Quand on saisit un palindrome
#         msg = "radar"
#         # Alors celui-ci est renvoyé et bien dit est envoyé ensuite
#         msg += " bien dit"
#         self.assertEqual("radar bien dit", msg)
#     def test_bjr(self):
#         # Quand on envoie "bjr"
#         msg = "bjr"
#         print(msg)
#         # Alors celle-ci est renvoyée
#         self.assertEqual("bjr", msg)

if __name__ == '__main__':
    unittest.main()