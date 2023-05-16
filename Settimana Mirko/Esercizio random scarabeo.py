"""
ESERCIZIO: CREARE scarabeo
"""
from random import randint

class Scarabeo:
    lettere = "ABCDEFGHILMNOPQRSTUVZ"
    
    parola = ""

   ####################
    letteree = "AEIOU"
    def crea_parola(self):
        n = len(self.lettere)
        k = list()
        var_X = {'a': 1, 'b': 2, 'c': 3}
        parolacce = "ABCDEFGHILMNOPQRSTUVZ"
        nn = len(self.letteree)

        for x in range(2):
            self.parola += self.lettere[randint(0,n-1)]
            var_X['a'] = 4
            parolacce += 'b'
            self.parola += self.letteree[randint(0,nn-1)]
        print(self.parola)
        
parola = Scarabeo()
parola.crea_parola()