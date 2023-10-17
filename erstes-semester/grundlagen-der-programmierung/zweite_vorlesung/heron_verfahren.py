"""File contains an implementation for the Heron-Verfahren"""

def heron_verfahren(quadrat):
    # Heron Verfahren
    startwert = 2
    while abs(quadrat - (startwert**2)) > 1e-20:
        startwert = (startwert + (quadrat / startwert)) / 2

    return startwert