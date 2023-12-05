def variante_eins():
    iteration = 0
    zaehler = 0
    while iteration < 5:
        for zeichen in "hallo, welt":
            zaehler += 1
        print("Iteration " + str(iteration) + "; Zaehler ist: " + str(zaehler))
        iteration += 1

def variante_zwei():
    for iteration in range(5):
        zaehler = 0
        while True:
            for zeichen in "hallo, welt":
                zaehler += 1
            print("Iteration " + str(iteration) + "; Zaehler ist: " + str(zaehler))

def variante_drei():
    for iteration in range(5):
        zaehler = 0
        while True:
            for zeichen in "hallo, welt":
                zaehler += 1
            print("Iteration " + str(iteration) + "; Zaehler ist: " + str(zaehler))
            break

def variante_vier():
    zaehler = 0
    text = "hallo, welt"
    for iteration in range(5):
        index = 0
    while index < len(text):
        zaehler += 1
        index += 1
    print("Iteration " + str(iteration) + "; Zaehler ist: " + str(zaehler))

