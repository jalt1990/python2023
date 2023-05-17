class Automezzo:
    # metodi

    tipo = ""
    n_ruote = 0

    # costruttore
    def __init__(self, tipo, n_ruote):
        self.tipo = tipo
        self.n_ruote = str(n_ruote)

    #metodo della classe
    def masterD(self):
        print("L' automezzo è del tipo " + self.tipo + " e ha " + self.n_ruote + ".")


# classe Figlio
class Veicolo(Automezzo):
    # metodi

    # costruttore
    def __init__(self, tipo, n_ruote, marca):
        super().__init__(tipo, n_ruote)
        self.marca = marca


    #metodo della classe
    def masterD(self):
        print("L' automezzo è del tipo " + self.tipo + " e ha " + self.n_ruote + " ruote.")


    def masterD_2(self):
        self.masterD()
        print("La marca è " + self.marca  + ".")


# classe Figlio del Figlio
class Modello(Veicolo):
    # metodi

    # costruttore
    def __init__(self, tipo, n_ruote, marca, nome):
        super().__init__(tipo, n_ruote, marca)
        self.nome = nome


    #metodo della classe

    def masterD_3(self):
        self.masterD_2()
        print("Il modello è " + self.nome  + ".")


auto = Modello("Autoveicolo", 4, "Alfa Romeo", "Stelvio")
auto.masterD_3()