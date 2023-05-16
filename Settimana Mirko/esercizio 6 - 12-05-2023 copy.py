'''Simulazione ristorante'''

class Cliente:
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.conto_cliente = {'ordini':{}, 'totale':0.00}

# flag avvio programma
flag_start = False

# inizializzare il menu e il conto
menu = {'antipasto':6.00, 'pasta':10.50, 'bistecca': 12.00, 'torta': 7.00}

listaconti = []

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
                cliente.nome = input("Inserisci il nome del cliente :")
                cliente.cognome = input("Inserisci il cognome del cliente :")
                piatto = input("Inserisci il nome del piatto: ")
                if piatto in menu:
                    quantita = int(input("Inserisci le quantita: "))
                    if piatto not in cliente.conto_cliente['ordini']:
                        cliente.conto_cliente['ordini'] |= {piatto : quantita}
                        cliente.conto_cliente['totale'] += menu[piatto] * quantita
                    else:
                        quantita_pregressa = cliente.conto_cliente['ordini'][piatto]
                        cliente.conto_cliente['ordini'] |= {piatto : quantita_pregressa + quantita}
                        cliente.conto_cliente['totale'] += menu[piatto] * quantita
                else:
                    print("\nIl piatto scelto non è nel menu.\n")
            
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
                listaconti.append(cliente)
                # ESCI
                print("\nArrivederci cliente\n\n")
                flag_cliente = True
            
            # VISIONARE I CONTI
            elif scelta_cliente == '5':
                print("\nConti dei clienti:\n")
                for cliente in listaconti:
                    print(f"{cliente.nome} {cliente.cognome} : {cliente.conto_cliente['totale']}€")
            
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