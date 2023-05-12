#Esercizio Bancomat, by Manuel Murtas & co.
 
u1_pin = '1234'
u2_pin = '5678'
 
utente_corrente = 0
counter_errore = 0
pin_ok = True
 
u1_conto = 50
u2_conto = 100
 
#saldo, prelevare, deposita, ci sono 2 conti e si puo fare bonifico, si fa iban corto per tutti e due
 
 
#prima parte per inserimento pin
while counter_errore < 4:
    pin_utente = input('inserire pin: ')
    
    if pin_utente == u1_pin:
        utente_corrente = 1
        break
    elif pin_utente == u2_pin:
        utente_corrente = 2
        break
    else:
        print('PIN errato, reinserire pin')
        counter_errore += 1
 
 
#parte per selezione operazione
if counter_errore == 4:
    print('Hai sbagliato troppe volte, riprova più tardi')
else:
    while pin_ok:
        print(f'Benvenuto utente {utente_corrente} ')
        scelta = input("""seleziona l'operazione: 
-premi 1 per prelevare: 
-premi 2 per visualizzare saldo:
-premi 3 per ricarica cellulare:
-premi 4 per fare bonifico:
-scrivi 'exit' per uscire""")
    
    # scelta exit
        if scelta == 'exit':
            pin_ok = False

        # scelta 1 (prelievo)    
        elif scelta == '1': 
            
            # stampa il saldo riconoscendo l'utente
            if utente_corrente == 1:
                print(f'Il tuo saldo è {u1_conto}.')
            else:
                print(f'Il tuo saldo è {u2_conto}.')
           
            # richiesta di prelievo
            scelta_prelievo = input('Digitare 0 per importo fisso, altrimenti digitare 1 per importo a scelta: \n')
           
            # importo fisso
            if scelta_prelievo == '0':
                ind_prelievoFisso = int(input("""quanto vuoi prelevare?: 
                -premi 1 per prelevare 20, 
                -premi 2 per prelevare 50,
                -premi 3 per prelevare 100.
                """))
            
                quantita_prelievi = [20, 50, 100]
                
                # controllo sul conto dell'utente
                if utente_corrente == 1:    #utente1
                    if u1_conto - quantita_prelievi[ind_prelievoFisso-1] < 0:
                        print('Non ci sono abbastanza soldi')
                    else:
                         u1_conto -= quantita_prelievi[ind_prelievoFisso - 1]
                elif utente_corrente == 2:  #utente2 
                    if u2_conto - quantita_prelievi[ind_prelievoFisso-1] < 0:
                        print('Non ci sono abbastanza soldi')
                    else:
                         u2_conto -= quantita_prelievi[ind_prelievoFisso - 1]
            
            # importo a scelta
            elif scelta_prelievo == '1':
                prelievo_var = int(input('Inserisci importo con multipli di 5:\n'))
                if prelievo_var % 5 != 0:
                    print('Hai inserito una somma errata')
                else:                                   
                    # controllo sul conto dell'utente
                    if utente_corrente == 1:    #utente1
                        if u1_conto - quantita_prelievi[ind_prelievoFisso-1] < 0:
                            print('Non ci sono abbastanza soldi')
                        else:
                            u1_conto -= quantita_prelievi[ind_prelievoFisso - 1]
                            print('saldo :', u1_conto)
                    elif utente_corrente == 2:  #utente2 
                        if u2_conto - quantita_prelievi[ind_prelievoFisso-1] < 0:
                            print('Non ci sono abbastanza soldi')
                        else:
                            u2_conto -= quantita_prelievi[ind_prelievoFisso - 1]
                            print('saldo :', u2_conto)
            pin_ok = False

        # scelta 2 (visualizza saldo)    
        elif scelta == '2':
            if utente_corrente == 1:
                print(f'saldo : {u1_conto}')
            else:
                print(f'saldo : {u2_conto}')