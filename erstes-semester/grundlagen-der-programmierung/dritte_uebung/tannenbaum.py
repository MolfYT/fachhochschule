def erstelle_tannenbaum(breite):
    """
    Erstellt einen Tannenbaum mit der angegebenen Breite.
    """
    for i in range(1, breite + 1, 2):
        print(" " * ((breite - i) // 2) + "*" * i)

    print((breite//2 - 1) * " " + "***")

ungerade_zahl = False

while not ungerade_zahl:
    nutzerEingabe = int(input("Geben Sie die Breite des Tannenbaums an: "))
    if nutzerEingabe % 2 == 0 or nutzerEingabe < 5:
        print("Bitte geben Sie eine ungerade Zahl >= 5 ein.")
        continue
    else:
        ungerade_zahl = True
else:
    erstelle_tannenbaum(nutzerEingabe)