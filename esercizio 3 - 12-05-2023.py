# inizializzazione delle variabili
frase = input('Inserisci la frase da analizzare:\n')

# pulizia della frase
punteggiatura = "!'*+[]§#@.,;:?^"
for carattere in punteggiatura:
    frase = frase.replace(carattere,'')

# lista delle parole in maiuscolo da contare
parole = frase.upper().split(' ')

# dizionario delle parole
conta_parole = dict()

# ciclo per creare il dizionario
for parola in parole:
    if parola not in conta_parole:
        conta_parole[parola] = parole.count(parola)

# stampa l'output
# output
print('Ecco a te il risultato della conta:\n')
print()

for chiave, valore in conta_parole.items():
    print(f"La parola <{chiave}> è presente {valore} volte nella frase.")


