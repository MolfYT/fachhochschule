def potenzierung_rekursiv(a, b, a_original = None):
    if b == 1:
        return a
    else:
        return potenzierung_rekursiv(a * (a_original if a_original else a), b - 1, a_original if a_original else a)
    
print(potenzierung_rekursiv(2, 3))