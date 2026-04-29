from Aufgabe5 import bisection



def tester():
    """
    Testfunktion, die die Bisektionsmethode mit einer Beispiel-Funktion testet und die Ergebnisse mit verschiedenen Genauigkeiten ausgibt.

    Rückgabewerte:
        - None
    """

    function_str = "2*x + x**2 + 3*x**3 - x**4"
    a = 2
    b = 5

    for epsilon in [10**-2, 10**-8]:
        c, fc, error_values, x_values, iterations = bisection(function_str, a, b, epsilon)

        print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")
        print(f"Anzahl der Iterationen für Genauigkeit von {epsilon}: {iterations}")
        print(f"Abweichung von der tatsächlichen Nullstelle: {abs(c - 3.4567)}")



if __name__ == "__main__":

    tester()