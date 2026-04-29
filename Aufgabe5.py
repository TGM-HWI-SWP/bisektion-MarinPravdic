import math



def solver() -> None:
    """
    Hauptfunktion, die die Benutzereingaben entgegennimmt, die Nullstelle anhand der Bisektionsmethode berechnet und das Ergebnis ausgibt.

    Rückgabewerte:
        - None
    """

    test_solver()

    # Benutzereingaben entgegennehmen
    function_str, a, b = get_inputs()
    epsilon = get_epsilon()
    c, fc, error_values, x_values, iterations = bisection(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")


def get_inputs() -> tuple:
    """
    Funktion, die die Benutzereingaben für die Funktion und die Intervallgrenzen entgegennimmt.

    Rückgabewerte:
        - function_str (string): der die Funktion repräsentiert (z.B. "x**2 - 4")
        - a (float): die erste Intervallgrenze
        - b (float): die zweite Intervallgrenze
    """

    # Funktionseingabe
    function_str = input("\nBitte geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

    # Intervallgrenzen eingeben
    while True:
        try:
            a = float(input("\nBitte geben Sie die erste Intervallsgrenze ein: "))
            b = float(input("Bitte geben Sie die zweite Intervallsgrenze ein: "))
            break
        
        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

    # Überprüfen, ob a < b
    if a >= b:
        print("\nDie erste Intervallsgrenze muss kleiner als die zweite sein.")
        exit()

    return function_str, a, b


def get_epsilon() -> float:
    """
    Funktion, die die gewünschte Genauigkeit (Epsilon) vom Benutzer entgegennimmt.

    Rückgabewerte:
        - epsilon (float): die gewünschte Genauigkeit (z.B. 10**-8)
    """

    # Genauigkeit eingeben
    while True:
        try:
            epsilon_exp = int(input("\nBitte geben Sie die gewünschte Genauigkeit ein (10^...): "))
            break
        
        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
    
    epsilon = 10**epsilon_exp   # Berechnung von Epsilon aus der Exponenteneingabe

    return epsilon


def function(x : float, function_str : str) -> float:
    """
    Funktion, die den Funktionswert für einen gegebenen x-Wert und eine Funktion als String berechnet.

    Parameter:
        - x (float): der Wert, für den der Funktionswert berechnet werden soll
        - function_str (string): der die Funktion repräsentiert (z.B. "x**2 - 4")

    Rückgabewerte:
        - eval(function_str): der berechnete Funktionswert für den gegebenen x-Wert
    """

    # Berechnung des Funktionswerts unter Verwendung von eval, wobei die wichtigsten mathematischen Funktionen und Konstanten zur Verfügung gestellt werden
    return eval(function_str, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sinh": math.sinh,
        "cosh": math.cosh,
        "exp": math.exp,
        "sqrt": math.sqrt,
        "log": math.log,
        "pi": math.pi,
        "e": math.e
    })


def bisection(function_str : str, a : float, b : float, epsilon : float) -> tuple:
    """
    Funktion, die die Bisektionsmethode zur Nullstellenbestimmung anwendet.

    Parameter:
        - function_str (string): die Funktion als String (z.B. "x**2 - 4")
        - a (float): die erste Intervallgrenze
        - b (float): die zweite Intervallgrenze
        - epsilon (float): die gewünschte Genauigkeit

    Rückgabewerte:
        - c (float): die näherungsweise Nullstelle
        - fc (float): der Funktionswert an der Nullstelle (sollte nahe 0 sein)
        - error_values (list): Liste der Fehlerwerte (|f(c)|) für jede Iteration
        - x_values (list): Liste der aktuellen Lösungen c für jede Iteration
        - iterations (int): die Anzahl der durchgeführten Iterationen
    """

    # Berechnung der Funktionswerte an den Intervallgrenzen
    fa = function(a, function_str)
    fb = function(b, function_str)

    # Listen zur Speicherung der Fehlerwerte und aktuellen Lösungen (relevant für die Visualisierung)
    error_values = []
    x_values = []

    # Überprüfen, ob die Funktion an den Intervallgrenzen unterschiedliche Vorzeichen hat (d.h. eine Nullstelle enthält)
    if fa * fb > 0:
        print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass die Nullstelle enthält.")
        exit()

    # Initialisierung der Mitte des Intervalls und des Funktionswerts an dieser Stelle
    c = (a + b) / 2
    fc = function(c, function_str)

    # Fehler und aktuelle Lösung zur Visualisierung speichern (relevant für die Visualisierung)
    error_values.append(abs(fc))
    x_values.append(c)
    
    iterations = 0  # Zähler für die Anzahl der Iterationen (relevant für Aufgabe 8)

    # Hauptschleife der Bisektionsmethode, die so lange läuft, bis der Funktionswert an c kleiner als epsilon ist
    while abs(fc) >= epsilon:
        # Überprüfen, ob einer der Intervallgrenzen oder die Mitte die Nullstelle ist
        if fa == 0:
            return a, fa, error_values, x_values, iterations
        elif fb == 0:
            return b, fb, error_values, x_values, iterations
        elif fc == 0:
            return c, fc, error_values, x_values, iterations

        # Bestimmen, in welchem Intervall die Nullstelle liegt, und die Intervallgrenzen entsprechend anpassen
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        # Berechnung der neuen Mitte des Intervalls und des Funktionswerts an dieser Stelle
        c = (a + b) / 2
        fc = function(c, function_str)

        error_values.append(abs(fc))
        x_values.append(c)

        iterations += 1

    return c, fc, error_values, x_values, iterations


def test_solver() -> None:
    """
    Testfunktion, die die Bisektionsmethode mit verschiedenen Funktionen testet.

    Rückgabewerte:
        - None
    """

    # Testfälle mit verschiedenen Funktionen und Intervallen
    for n in [25, 81, 144]:
        function_str = f"x**2-{n}"
        a = 0
        b = n
        epsilon = 10**-8

        c, fc, error_values, x_values, iterations = bisection(function_str, a, b, epsilon)

        # Ausgabe der Ergebnisse für jeden Testfall
        print(f"\nTest für n = {n}")
        print(f"Numerisch: {c}")
        print(f"Analytisch: {n**0.5}")
        print(f"Ungenauigkeit: {abs(c - n**0.5)}")



if __name__ == "__main__":

    solver()