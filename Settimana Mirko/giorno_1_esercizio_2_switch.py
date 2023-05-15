"""
CREARE UNA FUNZIONE DEL BLOCCO SWITCH
CHE AL SUO INTERNO CONTENGA UN MENU
"""

def conta():
    return 'conta'

def switch_menu(diz_comandi, msg_benvenuto):
    # diz_comandi è un dizionario comando: istruzione
    # msg_benvenuto è il messaggio di benvenuto
    print(msg_benvenuto)
    for value in diz_comandi.values():
        print(value)
    while True:
        arg = input('Inserisci la tua scelta :')
        if arg in diz_comandi:
            return diz_comandi[arg]
        else:
            continue
    
diz_comandi = {
    '1' : conta(),
    '2' : "2. STAMPA",
    '3' : "3. EXIT" 
    }

msg_benvenuto = 'Benvenuto nel programma,'

print(switch_menu(diz_comandi, msg_benvenuto))