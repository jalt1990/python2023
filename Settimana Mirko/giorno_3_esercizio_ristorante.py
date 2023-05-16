'''Simulazione ristorante'''
# TASK: CREARE UN SISTEMA DI ORDINAMENTO AD OGGETTI
# SI POSSONO ORDINARE MAX 4 PIATTI FISSI, MODIFICARE UN PIATTO, O AVERE IL CONTO
# OGNI PIATTO HA NOME E PREZZO
# SE CHIEDIAMO IL CONTO, CI DEVE CHIEDERE NOME E COGNOME E POI STAMPARE IL TOTALE E PIATTI A SCHERMO POI RITORNIAMO AL MENU INIZIALE
# OGGETTO CON QUALI PIATTI, QUANTO HO SPESO, CHI HA SPESO
# Vai a far si che si possa eliminare e aggiungere alla lista un piatto (parte 2)
# Vai a far si che l'utente possa creare il suo profilo prima di poter ordinare (parte 3)

# Classe cliente che contiene il nome, il conto_cliente e il budget
class Cliente:
    def __init__(self):
        self.nominativo = ""
        self.conto_cliente = {'ordini':{}, 'totale':0.00}
        self.budget = 0.00


# flag avvio programma
flag_start = False

# inizializzare il menu e il conto
menu = {'antipasto':6.00, 'pasta':10.50, 'bistecca': 12.00, 'torta': 7.00}
conti_clienti = {}

# avvio programma
while not flag_start:

    # controllo user:
    print("Benvenuto, fai l'accesso con il tuo account:")
    print("1. Entra\n2. Esci")
    scelta = input("\nInserisci scelta: ")

    # caso ENTRA
    if scelta == '1':
        flag_cliente = False
        while not flag_cliente:
            print("\nBenvenuto")
            print("Cosa vuoi fare?")
            print("1. Ordina\n2. Aggiungi o modifica un piatto\n3. Rimuovi un piatto\n4. Chiedi il conto\n5. Visiona i conti dei clienti")
            scelta_cliente = input("Inserisci scelta: ")

            # VISIONARE IL MENU
            if scelta_cliente == '1':
                print("\nMENU DEL RISTORANTE:\n")
                for piatto, prezzo in menu.items():
                    print(f"{piatto} : €{prezzo}")
                print()            
                # EFFETTUARE ORDINI
                cliente = Cliente()
                cliente.nominativo = input("Inserisci il nome del cliente :")
                cliente.budget = float(input("Inserisci il tuo budget: "))
                while cliente.budget > 6:
                    piatto = input("Inserisci il nome del piatto: ")
                    if piatto in menu:
                        quantita = int(input("Inserisci le quantita: "))
                        if menu[piatto]*quantita < cliente.budget:
                            if piatto not in cliente.conto_cliente['ordini']:
                                cliente.conto_cliente['ordini'] |= {piatto : quantita}
                                cliente.conto_cliente['totale'] += menu[piatto] * quantita
                                cliente.budget -= cliente.conto_cliente['totale']
                            else:
                                quantita_pregressa = cliente.conto_cliente['ordini'][piatto]
                                cliente.conto_cliente['ordini'] |= {piatto : quantita_pregressa + quantita}
                                cliente.conto_cliente['totale'] += menu[piatto] * quantita
                                cliente.budget -= cliente.conto_cliente['totale']
                        else:
                            print('Non hai abbastanza budget per questo piatto')
                    else:
                        print("\nIl piatto scelto non è nel menu.\n")
                print('Hai finito il tuo budget.')
            
            # MODIFICARE O AGGIUNGERE PIATTI AL MENU
            elif scelta_cliente == '2':
                piatto = input("Inserisci il piatto: ")
                prezzo = float(input("Inserisci il prezzo: "))
                menu[piatto] = prezzo
                print(f"Hai aggiunto il piatto {piatto} a € {prezzo} nel menu.")
            
            # ELIMINARE UN PIATTO DAL MENU
            elif scelta_cliente == '3':
                piatto = input("Inserisci il piatto: ")
                del menu[piatto]
                print(f"Hai rimosso il piatto {piatto} a € {prezzo} dal menu.")
            
            # CHIEDERE IL CONTO
            elif scelta_cliente == '4':
                print("\nConto del cliente:\n")
                for piatto, quantita in cliente.conto_cliente['ordini'].items():
                    print(f"{piatto} : {quantita} pz")
                print("TOTALE : €", cliente.conto_cliente["totale"],"\n")
                conti_clienti[cliente.nominativo] = cliente.conto_cliente["totale"]
                # ESCI
                print("\nArrivederci cliente\n\n")
                flag_cliente = True
            
            # VISIONARE I CONTI
            elif scelta_cliente == '5':
                print("\nConti dei clienti:\n")
                for cliente in conti_clienti.keys():
                    print(f"{cliente} : {conti_clienti[cliente]}€")
            
            # ERRORE cliente            
            else:
                print("\nHai inserito una scelta non valida, riprova.\n")
    
    # ERRORE SCELTA UTENTE            
    elif scelta == '2':
        print("Grazie per aver usato RistoApp, Arrivederci!")
        flag_start = True

    # ERRORE SCELTA UTENTE            
    else:
        print("Hai inserito una scelta non valida, riprova.")