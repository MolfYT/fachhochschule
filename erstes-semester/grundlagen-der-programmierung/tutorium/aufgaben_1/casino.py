"""Dieses Programm testet, ob eine vom Benutzer eingegebene Zahl 42 ist, kleiner oder größer ist"""

def guess_number():
    """Funktion zum Zahlen raten"""
    try:
        user_number = float(input("Raten sie die geheime Zahl: "))
    except ValueError:
        return print("Das war keine Zahl. Versuche es erneut.")

    if user_number == 42.0:
        print("Die geheime Zahl war 42, Sie haben richtig geraten.")
    elif user_number < 42.0:
        print("Ihre geratene Zahl war keliner als die geheime Zahl.")
    elif user_number > 42.0:
        print("Ihre geratene Zahl war größer als die geheime Zahl.")

if __name__ == "__main__":
    guess_number()
