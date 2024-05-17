"""Aufgabe 01
"""

import math

def addition(zahl_a, zahl_b):
    """Addition
    """
    return zahl_a + zahl_b

def subtraktion(zahl_a, zahl_b):
    """Subtraktion
    """
    return zahl_a - zahl_b

def multiplikation(zahl_a, zahl_b):
    """Multiplikation
    """
    return zahl_a * zahl_b

def division(zahl_a, zahl_b):
    """Division
    """
    return zahl_a / zahl_b

def wurzel(zahl):
    """Wurzel
    """
    return math.sqrt(zahl)

def dritte_wurzel(zahl):
    """ Annahme: x, epsilon floats, epsilon > 0
    returns ergebnis: x-epsilon <= ergebnis**3 <= x+epsilon"""
    return zahl**(1/3)
    
def ersetzeUmlauteInText(text):
    """Ersetze Umlaute in Text
    """
    return text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss").replace("!", "").replace("?", "").replace("@", "")
