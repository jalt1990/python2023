def switch_menu(listaNomi, listaMetodi, msgBenvenuto):
    flag_start = False
    print(msgBenvenuto)
    numero_oggetti = len(listaNomi)

    for n in range(numero_oggetti):
        print(f"{n+1}. {listaNomi[n]}")
    
    while not flag_start:
        scelta = int(input('Inserisci la tua scelta: '))
        try:
            listaMetodi[scelta-1]
        except:
            continue

class Funzioni:
    def entra(self):
        print("entrato")

    def esci(self):
        print('sei uscito')

oggetto = Funzioni()
lista_1 = ["Entra", "Esci"]
lista_2 = [oggetto.entra(), oggetto.esci()]
msgBenvenuto = "Benvenuto"


switch_menu(lista_1, lista_2, msgBenvenuto)

   
