'''Scrivere un programma python per la gestione di un registro vendite 
   Il programma deve permettere di aggiungere le vendite di diversi prodotti
   e calcolare il totale delle vendite (per ogni prodotto)

   OPERAZIONI: 
   1) Aggiungi una vendita di un prodotto 
      (si richiede all'utente il nome del prodotto, la quantità ed il prezzo per unità)

   2) Visualizzare il totale delle vendite per ogni prodotto per presente nel registro
   Suggerimento: utilizzare un dizionario per memorizzare le vendite dei prodotti
   (le chiavi sono i nomi dei prodotti e i valori sono liste che contengono quantità e prezzo unitario)  '''

# flag di inizio programma
start_flag = False

# Inizializzazione del Registro:
registro = dict()

# avvio del programma e menu principale
while not start_flag:
    print('\nBenvenuto nel registro vendite,\nScegli cosa vuoi fare:')
    print('1. Aggiungi vendita\n2. Visualizza il totale delle vendite\n3. Esci')
    scelta = input("Inserisci il numero dell'azione da fare: ")

    # scelta del menu AGGIUNGI VENDITA
    if scelta == '1':
        vendite_flag = False
        while not vendite_flag:
            # opzioni menu
            print('\nBenvenuto nel menu AGGIUNGI VENDITA,')
            print('Cosa vuoi fare?\n')
            print('1. Aggiungi vendita\n2. Torna al menu precedente')
            scelta_2 = input()

            # inserisci prodotto
            if scelta_2 == '1':

                prodotto = input("Inserisci il nome del prodotto venduto:")
                quantita = int(input("Inserisci il numero delle vendite:"))
                prezzo = float(input("Inserisci il prezzo del prodotto:"))
                fatturato = quantita * prezzo
                
                # crea il prodotto nel registro
                if prodotto not in registro:
                    registro[prodotto] = {'quantita':quantita, 'prezzo': [prezzo], 'fatturato': fatturato}
                
                # aggiorna i dati delle vendite del prodotto
                else:
                    dati = registro[prodotto]
                    dati['quantita'] += quantita
                    dati['prezzo'] += [prezzo]
                    dati['fatturato'] += fatturato
                    registro[prodotto] = dati
                print('\nLa registrazione del prodotto è stata eseguita.\n')
            
            # torna al menu principale
            elif scelta_2 == '2':
                ('\nHai scelto di tornare al menu principale\n')
                vendite_flag = True
            
            # in caso di errore
            else:
                print('Hai inserito una scelta non valida, riprova.')
    
    # stampa del registro
    elif scelta == '2':
        print('\nTi riporto qui sotto i dati del registro vendite:')
        for prodotto, dati in registro.items():
            prezzo_medio = sum(dati['prezzo'])/len(dati['prezzo'])
            qta = dati['quantita']
            fatt = dati['fatturato']
            print(f"{prodotto}\t:\tn. {qta} pezzi venduti mediamente a € {prezzo_medio} per un fatturato di {fatt}")

    # uscita dal programma
    elif scelta == '3':
        print('\nGrazie di aver usato il software di gestione registro.\nArrivederci.\n')
        start_flag = True

    # errore
    else:
        print('Hai inserito una scelta non valida, riprova.')
        




