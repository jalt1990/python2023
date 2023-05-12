# flag di accesso
accesso = True

while accesso:
    # istruzioni
    print("Benvenuto al primo menu")
    print("Cosa vuoi fare?\n1.ACCEDI\n2.ESCI")
    # scelta
    scelta_main = input("Inserisci il numero dell'operazione: ")

    # apertura menù 1
    if scelta_main == '1':
        print('scelta 1')

        # MENU OPERAZIONI MATEMATICA
        
        # flag di calcolatrice
        calcolatrice = True
        
        # ciclo del secondo menu
        while calcolatrice:
            # istruzioni
            print("Hai fatto l'accesso alla calcolatrice")
            print("Cosa vuoi fare?\n1.ADDIZIONE\n2.SOTTRAZIONE\n3.MOLTIPLICAZIONE\n4.DIVISIONE\n5.TORNA AL MENU PRECEDENTE")

            # scelta
            scelta_calc = input("Inserisci il numero dell'operazione: ")
            
            # addizione
            if scelta_calc == '1':
                print('Hai scelto Addizione')
                x = float((input('Inserisci il primo addendo: ')))
                y = float((input('Inserisci il secondo addendo: ')))
                print('La somma è', x + y)
            
            # sottrazione
            elif scelta_calc == '2':
                print('Hai scelto Sottrazione')
                x = float((input('Inserisci il diminuendo: ')))
                y = float((input('Inserisci il sottraendo: ')))
                print('La differenza è', x - y)
            
            # moltiplicazione
            elif scelta_calc == '3':
                print('Hai scelto Moltiplicazione')
                x = float((input('Inserisci il fattore: ')))
                y = float((input('Inserisci il fattore: ')))
                print('Il prodotto è', x * y)
            
            # divisione
            elif scelta_calc == '4':
                print('Hai scelto Divisione')
                x = float((input('Inserisci il dividendo: ')))
                y = float((input('Inserisci il divisore: ')))
                if y == 0:
                    print('Non puoi dividere per zero: il quoziente è indeterminabile.')
                else:
                    print('Il quoziente è', x / y)
            
            # uscita
            elif scelta_calc == '5':
                print('Grazie per aver usato la calcolatrice, arrivederci')
                calcolatrice = False
            
            # errore
            else:
                print('Hai inserito una scelta errata, riprova per favore.')


    # uscita
    elif scelta_main == '2':
        print("Grazie e arrivederci")
        accesso = False
    else:
        print('Hai inserito una scelta errata, riprova per favore.')