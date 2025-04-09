numero = int(input("Inserisci un numero: "))

def calcolo_numeri_primi(numero):
    numeri_primi = []
    for num in range(2, numero + 1):  
        is_primo = True
        for divisore in range(2, int(num ** 0.5) + 1):  
            if num % divisore == 0:
                is_primo = False
                break
        if is_primo:
            numeri_primi.append(num)
    return numeri_primi

primi = calcolo_numeri_primi(numero)
conta = len(primi)
print(conta, "numeri primi: " + "fino a", numero)
print(primi)
