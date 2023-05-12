'''Scrivere un programma che prenda una lista di numeri come input 
   e rimuove i duplicati dalla lista, lasciando solo i valori "unici".
   L'ordine degli elementi nella lista deve rimanere invariato'''

# inizializzazione della lista numeri
numeri = input("scrivi i numeri separati da una virgola:")
numeri = numeri.replace(' ','')
numeri = numeri.split(',')

# inizializzazione della lista di output
output = [] # output = list() #lista


# esplorazione della lista numeri e aggiunge in coda soltanto se non presente
for numero in numeri:
    if numero in output:
        continue
    else:
        output.append(numero)

# output
print('la lista inserita è:\n', numeri)
print('togliendo occorrenze ridondandi diventa:\n', output)

# stringa da usare come esempio : 1,2,33,15,1,2,15,33,4
