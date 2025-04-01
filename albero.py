
lettera = input ("inserisci una lettera: ")
ampiezza = int(input("inserisci l'ampiezza: "))

base = lettera * ampiezza

print(" " * 5 + lettera * (ampiezza -10) + " " * 5)
print(" " * 4 + lettera * (ampiezza -8) + " " * 4)
print(" " * 3 + lettera * (ampiezza -6) + " " * 3)
print(" " * 2 + lettera * (ampiezza -4) + " " * 2)
print(" " + lettera * (ampiezza -2) + " ")
print(base)
print(" ")



