class Menu:
    # flag di inizio loop
    flag_start = False
    flag_cliente = False


    # Costruttore della classe
    def __init__(self, msgBenvenuto, dizComandi):
        self.msgBenvenuto = msgBenvenuto
        self.dizComandi = dizComandi
    
    def esciCliente(self):
        print("Grazie e arrivederci")
        self.flag_cliente = True
    
    # SWITCH - MENU
    def switch_main_menu(self):
        # diz_comandi è un dizionario {comando: istruzione}
        # msg_benvenuto è il messaggio di benvenutoe
        while not self.flag_start:
            print(self.msgBenvenuto)
            # per numero e funzione collegata nel dizionario:
            for numero, dizFunzione in self.dizComandi.items():
                nomeFunzione = list(dizFunzione.keys())[0]
                # stampa 1. funzione_uno
                print(f"{numero}. {nomeFunzione}")
            # comando Esci:
            ultimo_n = len(self.dizComandi)+1
            print(f"{ultimo_n}. ESCI")
            arg = input('Inserisci la tua scelta :')
            if arg in self.dizComandi.keys():
                # in base alla scelta fatta in arg, viene scelta la sottofunzione da avviare
                sottoFunzione = list(self.dizComandi[arg].values())[0]
                sottoFunzione
            elif arg == str(ultimo_n):
                self.esci()
            else:
                print("Input errato, riprova.")
                continue

    def switch_menu(self):
        # diz_comandi è un dizionario {comando: istruzione}
        # msg_benvenuto è il messaggio di benvenuto
        # cliente è oggetto ordinazione
        funzioni = Funzioni()
        cliente = funzioni.entra()
        print(self.msgBenvenuto, cliente.nome, cliente.cognome)
        # per numero e funzione collegata nel dizionario:

        for numero, dizFunzione in self.dizComandi.items():
            nomeFunzione = list(dizFunzione.keys())[0]
            # stampa 1. funzione_uno
            print(f"{numero}. {nomeFunzione}")
        while not self.flag_start:
            arg = input('Inserisci la tua scelta :')
            if arg in self.dizComandi.keys():
                # in base alla scelta fatta in arg, viene scelta la sottofunzione da avviare

                break
            else:
                print("Input errato, riprova.")
                continue

# classe ORDINAZIONE
class Ordinazione:
    menu = {
        "antipasto" : 5.50,
        "pasta" : 6.50,
        "carne" : 7.50,        
        "dolce" : 5.50
        }

    # crea un utente con attributi NOME, COGNOME, ORDINI={PIATTO:PEZZI}, TOTALE=0.00
    def __init__(self, nome, cognome, ordini={}, totale=0.00):
        self.nome = nome
        self.cognome = cognome
        self.ordini = ordini
        self.totale = totale
    
    # PERMETTE DI AGGIUNGERE GLI ORDINI ALL'UTENTE E AGGIORNARE IL TOTALE
    def ordina(self, ordine):
        self.ordini |= {ordine}
        self.totale += list(ordine.values())[0]
    
    # MANDA IN STAMPA GLI ORDINI E IL TOTALE DA PAGARE
    def chiedereConto(self):
        for piatto, quantita in self.ordini.items():
            print(f"{piatto} : {quantita} Pz")
        print(f"TOTALE : {self.totale} €")


# CLASSE FUNZIONI

class Funzioni():

    def entra(self):
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        cliente = Ordinazione(nome, cognome)
        return cliente
    
    def ordina(self):
        pass

    def chiedereIlConto(self):
        pass

    def chiedereIlConto(self):
        pass

    def modificaIlMenu(self):
        pass



# BANCO DI PROVA

funzione = Funzioni()

msgOrdinazioni = "Menu Ordinazioni, scegliere il numero dell'operazione:"
sceltaOrdinazioni = {
    "1" : {"ORDINA": funzione.ordina()},
    "2" : {"MODIFICA PIATTO": funzione.chiedereIlConto()},
    "3" : {"CHIEDI IL CONTO": funzione.modificaIlMenu()},
    }
menuOrdinazioni = Menu(msgOrdinazioni, sceltaOrdinazioni)


msgIniziale = "Ciao, scegli il numero dell'operazione da eseguire:"
sceltaMenu = {"1" : {"ENTRA": menuOrdinazioni.switch_menu()}}
mainMenu = Menu(msgIniziale, sceltaMenu)
mainMenu.switch_main_menu()

