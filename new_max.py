import os  
from os import getcwd

percorso = getcwd()
print(f"Percorso corrente: {percorso}")
print("-" * 10)


file = input("Inserisci il nome del file: ")
print(f"<{file}>")


if os.path.exists(file):  
    with open(file, 'r') as f:  
        righe = f.readlines()

    numeri = [float(line.strip()) for line in righe]

    media = sum(numeri) / len(numeri) if numeri else 0

    valore_massimo = max(numeri)
    indice = numeri.index(valore_massimo) + 1

    
    print(f"Media: {media}")
    print(f"Valore massimo: {valore_massimo}")
    print(f"Numero della riga del valore massimo: {indice}")
else:
    print("File non trovato")