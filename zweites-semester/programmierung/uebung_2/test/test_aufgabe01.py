"""Tests Aufgabe 06
"""
import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, fr"{os.getenv("PROG_SRC_PATH")}")
import aufgabe01 # type: ignore
import pytest

def helper_test_equals(number_a, number_b, epsilon=0.001):
    """Prüfe Gleichheit der Zahhlen im Rahmen von Epsilon

    Args:
        number_a (float): Zahl A
        number_b (float): Zahl B
        epsilon (float, optional): maximal erlaubte Differenz. Defaults to 0.001.

    Returns:
        boolean: True, falls abs(number_a-number_b)<epsilon
    """
    return abs(number_a-number_b) < epsilon


def test_addition():
    """Test der Addition

    Äquivalenzklassen:
    Beschreibung        | zahl_a    | zahl_b    | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Zahlen kleiner Null | 0.1       | 0.2       | 0.3  
    Zahlen größer 1     | 2         | 3         | 5
    ...

    """

    assert (helper_test_equals(aufgabe01.addition(0.1, 0.2), 0.3))
    assert (helper_test_equals(aufgabe01.addition(2, 3), 5))

def test_subtraktion():
    """Test der Subtraktion

    Äquivalenzklassen:
    Beschreibung        | zahl_a    | zahl_b    | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Zahlen > und < 0    | 1.1       | 0.001     | 1.099  
    ...
    """
    assert (helper_test_equals(aufgabe01.subtraktion(1.1, 0.001), 1.099))

def test_multiplikation():
    """Test der Multiplikation

    Äquivalenzklassen:
    Beschreibung        | zahl_a    | zahl_b    | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Zahlen > und < 0    | 1.1       | 0.001     | 0.0011  
    Zahl_a = 0          | 0         | 0.001     | 0
    Zahl_a = -1         | -1        | 0.001     | -0.001
    ...
    """
    assert (helper_test_equals(aufgabe01.multiplikation(1.1, 0.001), 0.0011))
    assert (helper_test_equals(aufgabe01.multiplikation(0, 0.001), 0))
    assert (helper_test_equals(aufgabe01.multiplikation(-1, 0.001), -0.001))

def test_division():
    """Test der Division

    Äquivalenzklassen:
    Beschreibung        | zahl_a    | zahl_b    | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Zahlen > 1          | 1.1       | 0.001     | 1100
    Zahlen < 1          | 0.1       | 0.001     | 100
    Zahlen < 0          | -1        | 0.001     | -1000
    ...
    """
    assert (helper_test_equals(aufgabe01.division(1.1, 0.001), 1100))
    assert (helper_test_equals(aufgabe01.division(0.1, 0.001), 100))
    assert (helper_test_equals(aufgabe01.division(-1, 0.001), -1000))

def test_wurzel():
    """Test der Wurzel

    Äquivalenzklassen:
    Beschreibung        | zahl      | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Zahl > 0            | 4         | 2
    Zahl = 0            | 0         | 0
    ...
    """
    assert (helper_test_equals(aufgabe01.wurzel(4), 2))
    assert (helper_test_equals(aufgabe01.wurzel(0), 0))

def test_dritte_wurzel():
    """Test der dritten Wurzel

    Äquivalenzklassen:
    Beschreibung        | zahl      | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Zahlen > 1          | 8         | 2
    Zahlen > 0 und < 1  | 0.125     | 0.5
    ...    
    """
    assert (helper_test_equals(aufgabe01.dritte_wurzel(8), 2))
    assert (helper_test_equals(aufgabe01.dritte_wurzel(0.125), 0.5))

def test_ersetzeUmlauteInText():
    """Test der ersetzeUmlauteInText

    Äquivalenzklassen:
    Beschreibung                 | text      | Erwartetes Ergebnis
    -----------------------------------------------------------------
    Umlaute                      | "äöüß"     | "aeoeuess"
    Sonderzeichen                | "!?@"       | ""
    Umlaute und Sonderzeichen    | "äöüß!?@"   | "aeoeuess"
    """
    assert (aufgabe01.ersetzeUmlauteInText("äöüß") == "aeoeuess")
    assert (aufgabe01.ersetzeUmlauteInText("!?@") == "")
    assert (aufgabe01.ersetzeUmlauteInText("äöüß!?@") == "aeoeuess")