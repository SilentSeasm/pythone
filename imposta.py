reddito = input("Inserisci il tuo reddito: ")
reddito = int(reddito)

#if type(reddito) != int:
#   print("Il reddito deve essere un numero intero. Riprova")

if reddito <= 28000:
    imposta = (reddito / 100) * 23
    print("Imposta da pagare al 23%:", imposta)
elif reddito <= 50000:
    imposta = (reddito / 100) * 35
    print("Imposta da pagare al 35%:", imposta)
elif reddito <= 75000: 
    imposta = (reddito / 100) * 43
    print("Imposta da pagare al 43%:", imposta)
else:  
    imposta = (reddito / 100) * 43  
    print("Imposta da pagare al 43%:", imposta)
