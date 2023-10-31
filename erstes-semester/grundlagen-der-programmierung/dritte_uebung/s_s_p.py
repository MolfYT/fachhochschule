# bindet ein Modul ein – bitte Zeile ignorieren
import random

print("Lass uns Schere, Stein, Papier spielen!")
schereString = "Schere"
steinString = "Stein"
papierString = "Papier"

# optionen beinhaltet nun eine Liste mit den drei zulässigen cEingabe-Optionen
optionen = (schereString, steinString, papierString)

# random.choice(optionen) beinhaltet einen zufällig gewählten Eintrag aus der Liste der Eingabe-Optionen
computerEingabe = random.choice(optionen)

def spieler_hat_gewonnen(eingabe1, eingabe2):
    if eingabe1 == eingabe2:
        return False
    elif (eingabe1 == "Schere" and eingabe2 == "Papier") or (eingabe1 == "Stein" and eingabe2 == "Schere") or (eingabe1 == "Papier" and eingabe2 == "Stein"):
        return False
    else:
        return True

# ab hier folgt nun Ihr eigener Code
gewonnen = False
while not gewonnen:
    nutzerEingabe = input("Wählen Sie Schere, Stein oder Papier: ")
    if nutzerEingabe not in optionen:
        print("Fehlerhafte Eingabe!")
        continue

    if nutzerEingabe == computerEingabe:
        print(f"Unentschieden - Sie hatten {nutzerEingabe}, der Computer hatte {computerEingabe}")
        computerEingabe = random.choice(optionen)
        continue

    gewonnen = spieler_hat_gewonnen(computerEingabe, nutzerEingabe)
    if not gewonnen:
        print(f"Sie haben mit {nutzerEingabe} verloren, der Computer hatte {computerEingabe}.")
        computerEingabe = random.choice(optionen)
        continue
else:
    print(f"Sie haben mit {nutzerEingabe} gewonnen, der Computer hatte {computerEingabe}.")