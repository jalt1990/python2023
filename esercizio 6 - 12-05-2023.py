'''Simulazione ristorante'''

# flag avvio programma
flag_start = False

# flag degli user
flag_ristoratore = False
flag_cliente = False

# password ristoratore
password = 'Antani'

# inizializzare il menu e il conto
menu = {'pasta':10.50, 'bistecca': 12.00, 'torta': 7.00}
conto_cliente = {'tavolo':1,'ordini':{}}

# avvio programma
while not flag_start:

    # controllo user:
    print("Benvenuto, fai l'accesso con il tuo account:")
    print("1. Ristoratore\n2. Cliente")
    utente = input("\nInserisci scelta: ")

    # caso RISTORATORE
    if utente == '1':
        print("\nInserisci password:")
        pass_user = input()

        # se la password è corretta:
        if pass_user == password:
            print("Benvenuto Ristoratore")
            print("Cosa vuoi fare?")
            print("1. Aggiornare il MENU\n2. Visiona il MENU\n3. Visionare il conto del cliente")
            scelta_menu_1 = input("Inserisci scelta: ")

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
                    print(f"{piatto}\t€{prezzo}")
            
            # VISIONARE IL CONTO DEL CLIENTE
            elif scelta_menu_1 == '3':
                print(f"Conto del tavolo {conto_cliente['tavolo']}: ")

        # se la password è errata:
        else:
            print("Password errata!\n")
            print("Torna al menu principale\n\n")           
    # caso CLIENTE
    elif utente == '2':
        print("Benvenuto Cliente")
        print("Cosa vuoi fare?")
        print("1. Visiona il MENU\n2. Ordina")
        scelta_menu_2 = input("Inserisci scelta: ")

        # VISIONARE IL MENU
        if scelta_menu_2 == '1':
            print("MENU DEL RISTORANTE:")
            for piatto, prezzo in menu.items():
                print(f"{piatto}\t€{prezzo}")
        
        elif scelta_menu_2 == '2':
            

    else:
        print("Hai inserito una scelta non valida, riprova.")
