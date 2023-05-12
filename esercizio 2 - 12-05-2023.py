'''Scrivi un programma che richieda all'utente di inserire una stringa
   e che conti quante volte ogni lettera appare nella stringa. 
   Il programma dovrebbe quindi creare un dizionario in cui le chiavi
   sono le lettere presenti nella stringa e 
   i valori sono il numero di volte che ogni lettera appare '''

# inizializziamo gli oggetti
stringa = input('Inserisci una stringa: ')
dizionario = dict()

# ciclo per creare il dizionario
for carattere in stringa:
    if carattere not in dizionario:
        dizionario[carattere] = stringa.count(carattere)

# output
print('Ecco a te il risultato della conta:')
for chiave, valore in dizionario.items():
    print(f"{chiave} è prsente {valore} volte nella stringa.")