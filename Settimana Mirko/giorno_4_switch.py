def switch():
    flag_start = False
    while not flag_start:
        print('Ciao, scegli tra le seguenti opzioni: ')
        print('1.\n2.\n3.\n4. Esci')
        scelta = input("scegli l'opzione: ")
        if scelta == '1':
            pass
        elif scelta == '2':
            pass
        elif scelta == '3':
            pass
        elif scelta == '4':
            print('Hai scelto di uscire, a presto!')
            break
        else:
            print("Errore: hai inserito un input errato.")
            continue

switch()