def addition_rekursiv(a, b):
    if b == 0:
        return a
    else:
        return addition_rekursiv(a + 1, b - 1)
    
print(addition_rekursiv(3, 4))