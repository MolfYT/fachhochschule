eingabe_a = int(input("Beantworten Sie die Frage mit Ja? (1/0): ")) == 1
eingabe_b = int(input("Beantworten Sie die Frage mit Ja? (1/0): ")) == 1

if eingabe_a == eingabe_b:
    print("Die beiden Befragten sind sich einig.")
elif eingabe_a:
    print("Nur Person A sagte ja.")
else:
    print("Nur Person B sagte ja.")
