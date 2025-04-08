lista = []

inputTrue = input("inserisci un numero: ")

while inputTrue != "q":

    lista.append(int(inputTrue))
    inputTrue = input("inserisci un numero: ")
    
    print("Il numero massimo attuale è:", max(lista))

print("Hai finito. La lista finale è:", lista)