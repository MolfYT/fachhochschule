eingabe_a = int(input("Beantworten Sie die Frage mit Ja? (1/0): "))
eingabe_b = int(input("Beantworten Sie die Frage mit Ja? (1/0): "))

if eingabe_a == 1:
    eingabe_a = True
else: 
    eingabe_a = False

if eingabe_b == 1:
    eingabe_b = True
else:
    eingabe_b = False    

if eingabe_a == eingabe_b:
    print("Die beiden Befragten sind sich einig.")
elif eingabe_a:
    print("Nur Person A sagte ja.")
else:
    print("Nur Person B sagte ja.")
