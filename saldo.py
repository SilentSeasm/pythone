anni = int(input("saldo dopo quanti anni? "))
saldo_iniziale = 1000
def saldo(saldo, tasso, anni):
    if anni == " ":
        
        for i in range(1, 21):
            saldo = saldo * (1 + tasso)
            print(f"Il saldo dopo {i + 1} anni è: {saldo:.2f}")
    else:
       
        for i in range(anni):
            saldo = saldo * (1 + tasso)
        return saldo
    

risultato = saldo(saldo_iniziale, 0.04, anni)

print(f"Il saldo finale dopo 10 anni è: {risultato:.2f}")
