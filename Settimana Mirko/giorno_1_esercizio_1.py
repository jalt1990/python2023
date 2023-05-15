"""
Usare loop per fare 
    1. conta
    2. stamp
    3. end

    in conta: arrivano 2 input numerici e 1 input operazionale
        alla fine stampa la somma dei 3 risultati
    in stamp: vengono stampate le operazioni singole e il totale
    in end: si chiude il programma
"""

# Creazione della classe Risposte:
class Risposte:
    sommatoria = 0
    operazioni = ""
    parziale = 0

    def somma(self, x, y):
        return x + y

    def sottrazione(self, x, y):
        return x - y

    def moltiplicazione(self, x, y):
        return x * y

# Creazione di un oggetto di tipo Risposte:
ans = Risposte()

flag_start = False


# AVVIO LOOP MAIN
while not flag_start:
    print("Ciao, scegli il numero dell' operazione da eseguire:")
    print("1. CONTA\n2. STAMP\n3. PULISCI\n4. ESCI")
    scelta_main = input("Scelta: ")

    # AVVIO LOOP CONTA
    if scelta_main == "1":
        contatore = 0
        ans.parziale = 0
        while contatore < 3:
            
            print("\nScegli l'operazione che vuoi eseguire:")
            print("1. ADDIZIONE\n2. SOTTRAZIONE\n3. MOLTIPLICAZIONE")

            # area input dell'utente --> operazione / operando1 / operando2
            scelta_conta = input("Scelta: ")
            numero_1 = float(input("Inserisci il primo numero: "))
            numero_2 = float(input("Inserisci il secondo numero: "))

            # scelta dell'operazione matematica
            if scelta_conta == "1":
                risultato = ans.somma(numero_1, numero_2)
                ans.operazioni += f"{numero_1} + {numero_2} = {risultato}\n"

            elif scelta_conta == "2":
                risultato = ans.sottrazione(numero_1, numero_2)
                ans.operazioni += f"{numero_1} - {numero_2} = {risultato}\n"

            elif scelta_conta == "3":
                risultato = ans.moltiplicazione(numero_1, numero_2)
                ans.operazioni += f"{numero_1} * {numero_2} = {risultato}\n"

            else:
                print("input errato, faccio io la somma :)")
                risultato = ans.somma(numero_1, numero_2)
                ans.operazioni += f"{numero_1} + {numero_2} = {risultato}\n"

            contatore += 1
            ans.parziale += risultato
            ans.sommatoria += risultato

        print(f"La sommatoria di questi risultati è {ans.parziale}")
        ans.operazioni += f"La sommatoria dei risultati è {ans.sommatoria}."
    
    # STAMPA DI TUTTE LE OPERAZIONI
    elif scelta_main == '2':
        if ans.operazioni == "":
            print("Non sono state fatte operazioni fino ad ora.")
        else:
            print(ans.operazioni)
    
    # PULIZIA DELLE OPERAZIONI
    elif scelta_main == '3':
        print("Sei sicuro di voler cancellare tutto?")
        risposta = input("Si/No :")
        if risposta == "Si":
            ans.operazioni = ""
            ans.sommatoria = 0
        elif risposta == "No":
            print("Nulla verrà cambiato")
        else:
            print("Non hai inserito un input accettabile")

    # ESCI
    elif scelta_main == '4':
        print("Grazie e arrivederci")
        flag_start = True

    else:
        print("Scelta errata, prego riprova.")