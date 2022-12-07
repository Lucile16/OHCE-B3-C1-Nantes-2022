from src.constants import constants

class ohce:
    def palindrome(self, mot):
        if mot == "" or mot is None:
            return "Bonjour, "
        elif mot == mot[::-1]:
            return "Bonjour, " + mot + " Bien dit !"
        return "Bonjour, " + mot[::-1]

    def langue(self, langue):
        if langue == "Fr":
            return constants.Bonjour
        elif langue == "En": 
            return constants.Hello

    # def palindrome(self, mot):
    #     return mot[::-1]