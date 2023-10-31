# Erstelle eine Liste mit den Zahlen von 1 bis 100
zahlen_liste = list(range(1, 101))

# Teile die Liste in 10er-Blöcke auf, um eine 10x10-Matrix zu erstellen
matrix = [zahlen_liste[i:i+10] for i in range(0, len(zahlen_liste), 10)]

# Gehe durch jede Zeile in der Matrix
for zeile in matrix:
    # Erstelle eine formatierte Zeichenkette für jede Zeile, 
    # wobei jede Zahl rechtsbündig in einem Feld von drei Zeichen ausgegeben wird
    formatierte_zeile = ' '.join("{:>3}".format(nummer) for nummer in zeile)
    
    # Drucke die formatierte Zeile
    print(formatierte_zeile)