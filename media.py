numero = 0 
somma = 0
contatore = 0

while True:
    numero = int(input("inserisci un numero: "))
    somma = somma + numero
    print("la somma è: ", somma)

    contatore = contatore + 1
    print("numeri inseriti fino ad ora: ", contatore)

    media = somma / contatore
    print("la media è: ", media)
    

