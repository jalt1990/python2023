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

def somma(x, y):
    return x + y

def sottrazione(x, y):
    return x - y

def moltiplicazione(x, y):
    return x * y

# Creazione della classe Risposte:
class Risposte:
    sommatoria = 0
    operazioni = ""

# Creazione di un oggetto di tipo Risposte:
ans = Risposte()

flag_start = False


# AVVIO LOOP MAIN
while not flag_start:
    print("Ciao, scegli il numero dell' operazione da eseguire:")
    print("1. CONTA\n2. STAMP\n3. ESCI")
    scelta_main = input("Scelta: ")

    # AVVIO LOOP CONTA
    if scelta_main == "1":
        conta_flag = 0
        sommatoria = 0
        while conta_flag < 3:
            operazioni = ""
            print("\nScegli l'operazione che vuoi eseguire:")
            print("1. ADDIZIONE\n2. SOTTRAZIONE\n3. MOLTIPLICAZIONE")

            # area input dell'utente --> operazione / operando1 / operando2
            scelta_conta = input("Scelta: ")
            numero_1 = float(input("Inserisci il primo numero: "))
            numero_2 = float(input("Inserisci il secondo numero: "))

            # scelta dell'operazione matematica
            if scelta_conta == "1":
                risultato = somma(numero_1, numero_2)
                ans.operazioni += f"{numero_1} + {numero_2} = {risultato}\n"
            elif scelta_conta == "2":
                risultato = sottrazione(numero_1, numero_2)
                ans.operazioni += f"{numero_1} - {numero_2} = {risultato}\n"
            elif scelta_conta == "3":
                risultato = moltiplicazione(numero_1, numero_2)
                ans.operazioni += f"{numero_1} * {numero_2} = {risultato}\n"
            else:
                print("input errato, faccio io la somma :)")
                risultato = somma(numero_1, numero_2)
                ans.operazioni += f"{numero_1} + {numero_2} = {risultato}\n"
            conta_flag += 1
            ans.sommatoria += risultato
        print(f"La sommatoria dei risultati è {ans.sommatoria}")
        ans.operazioni += f"La sommatoria dei risultati è {ans.sommatoria}."
    
    # STAMPA DI TUTTE LE OPERAZIONI
    elif scelta_main == '2':
        if ans.operazioni == "":
            print("Non sono state fatte operazioni fino ad ora.")
        else:
            print(ans.operazioni)
    
    elif scelta_main == '3':
        print("Grazie e arrivederci")
        flag_start = True

    else:
        print("Scelta errata, prego riprova.")