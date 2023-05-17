"""CREARE UNA CLASSE LISTAALLUNNI, che dovrà essere sempre valorizzata
appena si accede al primo menu,  Un primo menu con entra o esci, 
se esci si chiude tutto, se entri devi darmi X nomi obbligatori e X corrispettivi voti agli studenti,
L'esericizio sarà creare un sistema che permetta di
andare a scegliere un singolo utente e di modificare e aggiungere i suoi voti """

class Registro:
    # creazione del registro:
    def __init__(self, dizionarioAlunni = {} ):
        self.dizionarioAlunni = {}

    def switch(self):
        flag_start = False
        while not flag_start:
            print('Hai avviato il Registro: ')
            print('1. Entra\n2. Esci')
            scelta = input("scegli l'opzione: ")
            if scelta == '1':
                self.inserisciNelRegistro()
            elif scelta == '2':
                print('Hai scelto di uscire, a presto!')
                break
            else:
                print("Errore: hai inserito un input errato.")
                continue

        
    def inserisciNelRegistro(self):
        print('Hai scelto di inserire i voti: ')
        numero_studenti = int(input('Inserisci il numero degli studenti a cui dare il voto: '))
        for x in range(numero_studenti):
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            voto = int(input("Inserisci il voto: "))
            self.dizionarioAlunni[(nome, cognome)] = voto
        print("Hai inserito " + str(numero_studenti) + " studenti.")
            



class Alunno(Registro):

    # costruttore
    def __init__(self, nome, cognome, eta, registro):
        super().__init__(self)
        self.registro = registro
        self.dizionarioAlunni = registro.dizionarioAlunni
        self.nome = nome
        self.cognome = cognome
        self.eta = str(eta)

    #metodo della classe
    def controllo(self):
        studente = (self.nome, self.cognome)
        if studente in registro.dizionarioAlunni:
            print("Lo studente è nel registro e il suo voto è :", registro.dizionarioAlunni[studente])
        else:
            print("Studente non presente in registro")




registro = Registro()
registro.switch()
print(registro.dizionarioAlunni)
alunno = Alunno("Franco", "Rinaldi", 33, registro)
alunno.controllo()
