"""
ESERCIZIO: CREARE UN DADO A 20 FACCE
"""
from random import randint

class Dado:
    n_facce = 0
    n_superficie = 0

    def __init__(self, n_facce):
        self.n_facce = n_facce
    
    def lancia_dado(self):
        return randint(1, self.n_facce)
    

dado_fortuna = Dado(20)
print(f"Hai lanciato il dado a {dado_fortuna.n_facce} facce.\nE' uscito il numero {dado_fortuna.lancia_dado()}")

    

