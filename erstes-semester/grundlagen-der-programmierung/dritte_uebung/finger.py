eingabe = int(input("Geben Sie eine natürliche Zahl ein: "))

def aufgabe_eins(eingabe):
    summe = 0
    for i in range(1, eingabe + 1):
        summe += i
    print(f"Alle Zahlen von 1 bis {eingabe} addiert ergeben {summe}.")

def aufgabe_zwei(eingabe):
    summe = 0
    for i in range(1, 100, eingabe):
        summe += i
    print(f"Jede n-te Zahl von 1 bis 100 addiert ergeben {summe}.")

def ist_primzahl(eingabe):
    for i in range(2, eingabe):
        if eingabe % i == 0:
            return False
    return True

def aufgabe_drei(eingabe):
    primzahlen = []
    for i in range(2, eingabe+1):
        primzahl = ist_primzahl(i)
        if primzahl:
            primzahlen.append(i)
    
    print(f"Alle Primzahlen von 2 bis {eingabe} sind:")
    print(primzahlen)

def aufgabe_vier(eingabe):
    teilbar_durch_eingabe = []
    for i in range(1,101):
        if i % eingabe == 0:
            teilbar_durch_eingabe.append(i)

    print(f"Alle Zahlen von 1 bis 100, die durch {eingabe} teilbar sind:")
    print(teilbar_durch_eingabe)

aufgabe_eins(eingabe)
aufgabe_zwei(eingabe)
aufgabe_drei(eingabe)
aufgabe_vier(eingabe)