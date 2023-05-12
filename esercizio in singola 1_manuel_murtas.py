exit_flag = False

while not exit_flag:
    print("\nBuongiorno! Vuoi accedere al sistema? Selezionare l'opzione desiderata")
    print("1. Accedi")
    print("2. Esci")
    scelta = input("Inserisci la tua scelta: ")

    if scelta == '2':
        print("\nArrivederci!")
        exit_flag = True
    elif scelta == '1':
        access_flag = False
        while not access_flag:
            print("\nSeleziona l'operazione che vuoi eseguire")
            print("1. Addizione")
            print("2. Sottrazione")
            print("3. Moltiplicazione")
            print("4. Divisione")
            print("5. Torna indietro")
            scelta_operazione = input("Inserisci la tua scelta: ")

            if scelta_operazione == '5':
                access_flag = True
            elif scelta_operazione not in '1234':
                print("\nErrore, l'opzione da te selezionata non esiste")
            else:
                primo_valore = float(input("Inserire il primo valore: "))
                secondo_valore = float(input("Inserire il secondo valore: "))

                if scelta_operazione == '1':
                    print(f"\nIl risultato dell'addizione {primo_valore} + {secondo_valore} è {primo_valore + secondo_valore}")
                elif scelta_operazione == '2':
                    print(f"\nIl risultato della sottrazione {primo_valore} - {secondo_valore} è {primo_valore - secondo_valore}")
                elif scelta_operazione == '3':
                    print(f"\nIl risultato della moltiplicazione {primo_valore} * {secondo_valore} è {primo_valore * secondo_valore}")
                else:
                    if secondo_valore == 0:
                        print("\nErrore, non puoi dividere per 0")
                    else:
                        print(f"\nIl risultato della divisione {primo_valore} / {secondo_valore} è {primo_valore / secondo_valore}")
    else:
        print("\nErrore, l'opzione da te selezionata non esiste")