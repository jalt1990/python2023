# inizializzazione delle variabili
frase = input('Inserisci la frase da analizzare:\n')

# pulizia della frase
punteggiatura = "!'*+[]§#@.,;:?^-£$%&()="
for carattere in punteggiatura:
    frase = frase.replace(carattere,'')

# lista delle parole in maiuscolo da contare
parole = frase.upper().split(' ')

# pulizia di parole vuote
while '' in parole:
    parole.remove('')

# dizionario delle parole
conta_parole = dict()

# ciclo per creare il dizionario
for parola in parole:
    if parola not in conta_parole:
        conta_parole[parola] = parole.count(parola)

# stampa l'output
print('\nEcco a te il risultato della conta:')
print()

for chiave, valore in conta_parole.items():
    print(f"La parola <{chiave}> è presente {valore} volte nella frase.")


