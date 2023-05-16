# GIORNO 1:
# LEZIONE DI CLASSI E OGGETTI

# viene creata una classe Tazza
class Tazza():
    # attributo 'contenuto' di tipo stringa
    contenuto = 'Buzz-Cola'

class Bottiglia():
    # attributo 'capacitaInLitri' di tipo int // l'attributo è anche detto "variabile della classe"
    capacitaInLitri = 3

# viene creato un oggetto di tipo tazza
# viene creata una variabile e le viene associata il tipo Tazza
oggetto_1 = Tazza()
oggetto_2 = Tazza()
oggetto_3 = Tazza()

# modifica del contenuto dell'oggetto_1 (POLIMORFISMO):
oggetto_1.contenuto = 'Caffe'
# non avendo metodi "tipizzati", l'attributo può essere di qualsiasi tipo 
oggetto_2.contenuto = 10    # anche numerico

print(oggetto_1.contenuto)
print(oggetto_2.contenuto)
print(oggetto_3.contenuto)

print("\n\n\n")

###############
#  NOTA BENE  #
###############

variabile = oggetto_1.contenuto # creo una variabile del tipo del contenuto di oggetto 1 e dello stesso valore
oggetto = oggetto_1 # creo un oggetto identico a oggetto_1, della stessa classe, dello stesso tipo e con gli stessi attributi

###############
#  NOTA BENE  #
###############


# creazione della classe contenente molti tipi
class MultiType():
    numeroInt = 0
    numeroFloat = 0.0
    stringa = 'sono una stringa'
    booleano = False


# cambiare il contenuto degli attributi
oggettoMultiType = MultiType()
oggettoMultiType.numeroInt = 33
oggettoMultiType.numeroFloat = 5.55
oggettoMultiType.stringa = 'Franco'
oggettoMultiType.booleano = True


# mandare in stampa gli attributi dell'oggetto
print(oggettoMultiType.numeroInt)
print(oggettoMultiType.numeroFloat)
print(oggettoMultiType.stringa)
print(oggettoMultiType.booleano)


# mandare in stampa con una sola print, usando magari il booleano come condizione
if oggettoMultiType.booleano:
    print(f"Ho {oggettoMultiType.numeroInt} anni, possiedo {oggettoMultiType.numeroFloat} euro sul conto e mi chiamo {oggettoMultiType.stringa}")


####################### POMERIGGIO ################################

class Persona:
    name = ""
    age = 0    

    # unico metodo che viene eseguito se non chiamato
    # METODO COSTRUTTORE
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def stampa(self):
        print(f"Ciao, sono {self.name} e ho {self.age} anni.")

# creazione dell'oggetto Pippo

pippo = Persona("Pippo", 75)

# esecuzione della stampa:
pippo.stampa() # --> Ciao, sono Pippo e ho 75 anni.


def nomeCheVoglio(*kids):
    print("I nomi che mi hai dato sono", *kids)




