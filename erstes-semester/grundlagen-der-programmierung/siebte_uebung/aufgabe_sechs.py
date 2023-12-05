def ggt_iterativ(a,b):
    while b != 0:
        a_temp = b
        b = a % b
        a = a_temp

    return a

def ggt_rekursiv(a,b):
    if b == 0:
        return a
    else:
        return ggt_rekursiv(b, a%b)

print(ggt_iterativ(864, 483))
print(ggt_rekursiv(864, 483))