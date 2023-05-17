

class Persona:

    # attributi
    tipo = 'umano'

    # metodi

    # costruttore
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = str(eta)

    #metodo della classe
    def masterD(self):
        print("Ciao sono " + self.nome + " " + self.tipo)

    
# Creazion dell' oggetto x:
x = Persona("Mirko", 99)

# uso del metodo dell'oggetto:
x.masterD()


class Allievo(Persona):
    
    # costruttore:
    def __init__(self, nome, eta, grado):
        super().__init__(nome, eta)
        self.grado = grado
    
    tipo = "gatto"

    def masterD(self):
        print("Ciao sono " + self.nome + " e ho " + self.eta + " e sono di " + self.grado + " grado")



"""
Creare un eredita lineare di tre classi che stampi tre attributi proprietari singoli
"""
class Figlio(Allievo):

    # costruttore:
    def __init__(self, nome, eta, grado, tipoFiglio, padre):
        super().__init__(nome, eta, grado)
        self.tipoFiglio = tipoFiglio
        self.padre = padre
        self.grado = grado

    def masterD(self):
        print("Ciao sono " + self.nome + " e ho " + self.eta + " anni, e sono figlio di " + self.padre + " di tipo " + self.tipoFiglio + ". Sono cintura nera di " + self.grado + ".")


figlio1 = Figlio("Franco", 33, "primo Dan", "Secondo genito", "Franco senior")
figlio1.masterD()