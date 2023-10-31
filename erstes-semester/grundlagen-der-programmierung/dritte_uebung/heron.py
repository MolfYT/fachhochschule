def heron_verfahren(startwert, quadrat, max_iterationen=5):
    # Heron Verfahren
    iteration = 0
    while abs(quadrat - (startwert**2)) > 1e-5 and max_iterationen > iteration:
        startwert = (startwert + (quadrat / startwert)) / 2
        iteration += 1
        print(f"Iteration {iteration}: Wert von g: {startwert}")

    print(f"Die Wurzel aus {quadrat} beträgt näherungsweise {startwert}")
    return startwert

quadrat = int(input("Bestimme die Wurzel aus: "))
startwert = int(input("Starte mit dem folgenden Wert: "))
heron_verfahren(startwert, quadrat)