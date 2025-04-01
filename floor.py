paino_scelto = input("Scegli un piano: ")
piano_scelto = int(paino_scelto)  # Converte il piano scelto in un intero
piano_attuale = 0
if piano_scelto != 13:
    piano_attuale = piano_scelto
    print(piano_attuale)
elif piano_scelto == 13:
    piano_attuale = piano_scelto + 1
    print(piano_attuale)    