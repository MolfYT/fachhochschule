def pascalsche_dreieck(z, s):
    if s > z or s < 1:
        return 0
    elif z == 1 and s <= z:
        return 1
    else:
        return pascalsche_dreieck(z-1, s-1) + pascalsche_dreieck(z-1, s)

print(pascalsche_dreieck(8,5))
