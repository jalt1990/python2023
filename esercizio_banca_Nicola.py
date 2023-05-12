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
        premi 1 per prelevare: 
        premi 2 per visualizzare saldo:
        premi 3 per ricarica cellulare:
        premi 4 per fare bonifico:
        scrivi 'exit' per uscire""")
    
        if scelta == 'exit':
            pin_ok = False
        
        elif scelta == '1': 
            if utente_corrente == 1:
                print(f'Il tuo saldo è {u1_conto}.')
            else:
                print(f'Il tuo saldo è {u2_conto}.')
           
            
            prelievoOk = True
            while prelievoOk:
                scelta_prelievo = input('Digitare 0 per importo fisso, altrimenti digitare 1 per importo a scelta: \n')
                if scelta_prelievo == '0':
 
                    ind_prelievoFisso = int(input("""quanto vuoi prelevare?: 
                    premi 1 per prelevare 20: 
                    premi 2 per prelevare 50:
                    premi 3 per prelevare 100:
                    """))
 
                    quantita_prelievi = [20, 50, 100]
 
                    if utente_corrente == 1:
                        if u1_conto - quantita_prelievi[ind_prelievoFisso-1] < 0:
                            print('Non ci sono abbastanza soldi')
                        else:
                             u1_conto -= quantita_prelievi[ind_prelievoFisso - 1]
                    elif utente_corrente == 2:          
                        if u2_conto - quantita_prelievi[ind_prelievoFisso-1] < 0:
                            print('Non ci sono abbastanza soldi')
                        else:
                             u2_conto -= quantita_prelievi[ind_prelievoFisso - 1]
                    prelievoOk = False
                    
                elif scelta_prelievo == '1':
                    prelievo_var = input('digita la cifra che vuoi prelevare ricordando che deve essere un multiplo di 5: \n')
 
                    if int(prelievo_var)%5 != 0:
                        print('Perdona, reinizia')
                    else:
                        if utente_corrente == 1:
                            if u1_conto - int(prelievo_var) < 0:
                                print('Non ci sono abbastanza soldi')
                            else:
                                 u1_conto -= int(prelievo_var)
                        elif utente_corrente == 2:          
                            if u2_conto - int(prelievo_var) < 0:
                                print('Non ci sono abbastanza soldi')
                            else:
                                 u2_conto -= int(prelievo_var)
                    prelievoOk = False
               
                else:
                    prelievoOk = True
        pin_ok = False                    
 
print(u1_conto, u2_conto)