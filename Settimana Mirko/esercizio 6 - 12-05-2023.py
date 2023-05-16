'''Simulazione ristorante'''

# flag avvio programma
flag_start = False

# password ristoratore
password = 'Antani'

# inizializzare il menu e il conto
menu = {'pasta':10.50, 'bistecca': 12.00, 'torta': 7.00}
conto_cliente = {'ordini':{}, 'totale':0.00}

# avvio programma
while not flag_start:

    # controllo user:
    print("Benvenuto, fai l'accesso con il tuo account:")
    print("1. Ristoratore\n2. Cliente\n3. Esci")
    utente = input("\nInserisci scelta: ")

    # caso RISTORATORE
    if utente == '1':
        print("\nInserisci password:")
        pass_user = input()

        # se la password è corretta:
        if pass_user == password:
            flag_ristoratore = False
            while not flag_ristoratore:
                print()
                print("Benvenuto Ristoratore")
                print("Cosa vuoi fare?")
                print("1. Aggiornare il MENU\n2. Visiona il MENU\n3. Visionare il conto del cliente\n4. Far pagare il cliente\n5. Esci")
                scelta_menu_1 = input("\nInserisci scelta: ")
                print()

                # AGGIORNARE IL MENU
                if scelta_menu_1 == '1':
                    piatto = input("Inserisci il piatto: ")
                    prezzo = float(input("Inserisci il prezzo: "))
                    menu[piatto] = prezzo
                    print(f"Hai aggiunto il piatto {piatto} a € {prezzo} nel menu.")
                
                # VISIONARE IL MENU
                elif scelta_menu_1 == '2':
                    print("MENU DEL RISTORANTE:")
                    for piatto, prezzo in menu.items():
                        print(f"{piatto} : €{prezzo}")
                
                # VISIONARE IL CONTO DEL CLIENTE
                elif scelta_menu_1 == '3':
                    print("Conto del cliente:")
                    for piatto, quantita in conto_cliente['ordini'].items():
                        print(f"{piatto} : {quantita} pz")
                    print("TOTALE : €", conto_cliente["totale"])
                    
                # FAR PAGARE IL CONTO DEL CLIENTE
                elif scelta_menu_1 == '4':
                    print("Il cliente ha pagato il conto.")
                    conto_cliente = {'ordini':{}, 'totale':0.00}
                            
                # ESCI
                elif scelta_menu_1 == '5':
                    print("\nArrivederci Ristoratore\n")
                    flag_ristoratore = True
                
                # scelta non valida
                else:
                    print("Hai inserito una scelta non valida, riprova.")

        # se la password è errata:
        else:
            print("Password errata!\n")
            print("Torna al menu principale\n\n") 

    # caso CLIENTE
    elif utente == '2':
        flag_cliente = False
        while not flag_cliente:
            print("\nBenvenuto Cliente")
            print("Cosa vuoi fare?")
            print("1. Visiona il MENU\n2. Ordina\n3. Visiona ordini\n4. Esci")
            scelta_cliente = input("Inserisci scelta: ")

            # VISIONARE IL MENU
            if scelta_cliente == '1':
                print("\nMENU DEL RISTORANTE:\n")
                for piatto, prezzo in menu.items():
                    print(f"{piatto} : €{prezzo}")
                print()
            
            # EFFETTUARE ORDINI
            elif scelta_cliente == '2':
                piatto = input("Inserisci il nome del piatto: ")
                if piatto in menu:
                    quantita = int(input("Inserisci le quantita: "))
                    if piatto not in conto_cliente['ordini']:
                        conto_cliente['ordini'] |= {piatto : quantita}
                        conto_cliente['totale'] += menu[piatto] * quantita
                    else:
                        quantita_pregressa = conto_cliente['ordini'][piatto]
                        conto_cliente['ordini'] |= {piatto : quantita_pregressa + quantita}
                        conto_cliente['totale'] += menu[piatto] * quantita
                else:
                    print("\nIl piatto scelto non è nel menu.\n")
            
            # VISIONARE ORDINI
            elif scelta_cliente == '3':
                print("\nConto del cliente:\n")
                for piatto, quantita in conto_cliente['ordini'].items():
                    print(f"{piatto} : {quantita} pz")
                print("TOTALE : €", conto_cliente["totale"],"\n")

            # ESCI
            elif scelta_cliente == '4':
                print("\nArrivederci cliente\n\n")
                flag_cliente = True
            
            # ERRORE cliente            
            else:
                print("\nHai inserito una scelta non valida, riprova.\n")
    
    # ERRORE SCELTA UTENTE            
    elif utente == '3':
        print("Grazie per aver usato RistoApp, Arrivederci!")
        flag_start = True

    # ERRORE SCELTA UTENTE            
    else:
        print("Hai inserito una scelta non valida, riprova.")