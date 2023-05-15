"""
Usare loop per fare 
    1. conta
    2. stamp
    3. end

    in conta: arrivano 2 input numerici e 1 input operazionale
        alla fine stampa la somma dei 3 risultati
    in stamp: vengono stampate le operazioni singole e il totale
    in end: si chiude il programma

    PARTE 2:
    Aggiungere la possibilità di pulire i dati in memoria
"""

# Creazione della classe Risposte:
class Risposte:
    # da riportare nella stampa delle operazioni di CONTA
    parziale = 0
    # da riportare nella stampa di STAMP
    sommatoria = 0
    operazioni = ""
    
    # DEFINIZIONE DELLE OPERAZIONI MATEMATICHE
    def somma(self, listaInput):
        x = listaInput[0]
        y = listaInput[1]
        risultato = x + y
        self.operazioni += f"{x} + {y} = {risultato}\n"
        self.parziale += risultato
        self.sommatoria += risultato

    def sottrazione(self, listaInput):
        x = listaInput[0]
        y = listaInput[1]
        risultato = x - y
        self.operazioni += f"{x} - {y} = {risultato}\n"
        self.parziale += risultato
        self.sommatoria += risultato

    def moltiplicazione(self, listaInput):
        x = listaInput[0]
        y = listaInput[1]
        risultato = x * y
        self.operazioni += f"{x} * {y} = {risultato}\n"
        self.parziale += risultato
        self.sommatoria += risultato


# CLASSE MENU-SWITCH

class Menu:
    # flag di inizio loop
    flag_start = False


    # Costruttore della classe
    def __init__(self, msgBenvenuto, dizComandi):
        self.msgBenvenuto = msgBenvenuto
        self.dizComandi = dizComandi
    
    def esci(self):
        print("Grazie e arrivederci")
        self.flag_start = True
    
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
                sottoFunzione()
            elif arg == str(ultimo_n):
                self.esci()
            else:
                print("Input errato, riprova.")
                continue

    def switch_menu(self, nInput):
        # diz_comandi è un dizionario {comando: istruzione}
        # msg_benvenuto è il messaggio di benvenuto
        # nInput indica il numero di input dati dall'utente
        print(self.msgBenvenuto)
        # per numero e funzione collegata nel dizionario:
        for numero, dizFunzione in self.dizComandi.items():
            nomeFunzione = list(dizFunzione.keys())[0]
            # stampa 1. funzione_uno
            print(f"{numero}. {nomeFunzione}")
        while not self.flag_start:
            arg = input('Inserisci la tua scelta :')
            if arg in self.dizComandi.keys():
                # in base alla scelta fatta in arg, viene scelta la sottofunzione da avviare
                sottoFunzione = list(self.dizComandi[arg].values())[0]
                # le variabili di input vengono collezionate in una lista:
                listaInput = list()
                for n in range(nInput):
                    listaInput.append(float(input(f"Inserisci il {n+1}° numero: ")))
                # inserire funzione da eseguire con i numeri
                sottoFunzione(listaInput)
                break
            else:
                print("Input errato, riprova.")
                continue
    


# Classe Funzioni
class Funzioni:
    def __init__(self, ans):
        self.ans = ans
    # funzione CONTA
    def conta(self):
        self.ans.parziale = 0
        for x in range(3):
                
            msg = "\nScegli l'operazione che vuoi eseguire:"
            comandi = {
                "1" : {"ADDIZIONE" : self.ans.somma},
                "2" : {"SOTTRAZIONE": self.ans.sottrazione},
                "3" : {"MOLTIPLICAZIONE": self.ans.moltiplicazione}
                }

            # oggetto menu per conta:
            menuConta = Menu(msg, comandi)
            menuConta.switch_menu(2)
        # Stampa del Parziale:
        print(f"La sommatoria di questi risultati è {self.ans.parziale}\n\n")

    # funzione STAMPA TOTALI
    def stampaTotali(self):
        if self.ans.operazioni == "":
            print("Non sono state fatte operazioni fino ad ora.")
        else:
            print(self.ans.operazioni)
            print(f"La sommatoria dei risultati è {self.ans.sommatoria}.")


    # funzione PULIZIA DELLE OPERAZIONI
    def pulisciTutto(self):
        print("Sei sicuro di voler cancellare tutto?")
        risposta = input("Si/No :")
        if risposta == "Si":
            self.ans.operazioni = ""
            self.ans.sommatoria = 0
        elif risposta == "No":
            print("Nulla verrà cambiato")
        else:
            print("Non hai inserito un input accettabile")

    # funzione ESCI
    def esci(self):
        print("Grazie e arrivederci")
        menuMain.flag_start = True
        
        

    


# ======================== INIZIALIZZAZIONE OGGETTO E FLAG ===========================

# Creazione di un oggetto di tipo Risposte:
ans = Risposte()
funzioni = Funzioni(ans)



############################## ESECUZIONE DEL PROGRAMMA ############################

msgIniziale = "Ciao, scegli il numero dell' operazione da eseguire:"

sceltaMenu = {
    "1" : {"CONTA": funzioni.conta},
    "2" : {"STAMPA": funzioni.stampaTotali},
    "3" : {"PULISCI": funzioni.pulisciTutto}
    }

menuMain = Menu(msgIniziale, sceltaMenu)

# AVVIO LOOP MAIN
menuMain.switch_main_menu()
