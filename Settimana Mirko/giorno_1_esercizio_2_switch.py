"""
CREARE UNA FUNZIONE DEL BLOCCO SWITCH
CHE AL SUO INTERNO CONTENGA UN MENU
"""

def conta():
    return 'Conta'

def stampa():
    return 'Stampa'

def esci():
    return 'Esci'

def switch_menu(diz_comandi, msg_benvenuto):
    # diz_comandi è un dizionario {comando: istruzione}
    # msg_benvenuto è il messaggio di benvenuto
    print(msg_benvenuto)
    for numero, funzione in diz_comandi.items():
        print(f"{numero}. {funzione}")
    while True:
        arg = input('Inserisci la tua scelta :')
        if arg in diz_comandi:
            return diz_comandi[arg]
        else:
            continue
    
diz_comandi = {
    '1' : conta(),
    '2' : stampa(),
    '3' : esci() 
    }

msg_benvenuto = 'Benvenuto, questo è il menu funzioni:'

print(switch_menu(diz_comandi, msg_benvenuto))