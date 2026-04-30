from Aufgabe5 import get_inputs, get_epsilon, function



def solver2() -> None:
    """
    Hauptfunktion, die die Regula-Falsi-Methode implementiert und die Nullstelle einer Funktion findet. Es werden auch Testfälle für die Methode bereitgestellt.

    Rückgabewerte:
        - None
    """

    # Benutzeranweisungen
    print("=== Aufgabe 6: Regula-Falsi-Verfahren ===")
    print("Dieses Programm berechnet die Nullstelle einer Funktion mit der Regula-Falsi-Methode.")
    print("Geben Sie eine Funktion f(x) sowie ein Intervall [a, b] mit Vorzeichenwechsel ein.")
    print("Zusätzlich wählen Sie die gewünschte Genauigkeit (z.B. -6 für 10^-6).")
    test_solver2()

    # Benutzereingaben entgegennehmen
    function_str, a, b = get_inputs()
    epsilon = get_epsilon()
    c, fc, accuracy_values, x_values = regula_falsi(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")


def regula_falsi(function_str : str, a : float, b : float, epsilon : float) -> tuple:
    """
    Funktion, die die Regula-Falsi-Methode implementiert, um die Nullstelle einer Funktion zu finden.

    Parameter:
        - function_str (string): der die Funktion repräsentiert (z.B. "x**2 - 4")
        - a (float): die erste Intervallgrenze
        - b (float): die zweite Intervallgrenze
        - epsilon (float): die gewünschte Genauigkeit

    Rückgabewerte:
        - c (float): die näherungsweise Nullstelle
        - fc (float): der Funktionswert an der Nullstelle (sollte nahe 0 sein)
        - accuracy_values (list): Liste der Fehlerwerte (|f(c)|) für jede Iteration
        - x_values (list): Liste der aktuellen Lösungen c für jede Iteration
    """

    # Berechnung der Funktionswerte an den Intervallgrenzen
    fa = function(a, function_str)
    fb = function(b, function_str)

    # Listen zur Speicherung der Fehlerwerte und aktuellen Lösungen (relevant für die Visualisierung)
    accuracy_values = []
    x_values = []

    # Überprüfen, ob die Funktion an den Intervallgrenzen unterschiedliche Vorzeichen hat (d.h. eine Nullstelle enthält)
    if fa * fb > 0:
        print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass eine Nullstelle enthält.")
        exit()

    # Initialisierung der Stelle c anhand der Regula-Falsi-Formel und des Funktionswerts an dieser Stelle
    c = b - fb * ((b - a) / (fb - fa))
    fc = function(c, function_str)

    # Fehler und aktuelle Lösung zur Visualisierung speichern (relevant für die Visualisierung)
    accuracy_values.append(abs(fc))
    x_values.append(c)

    # Hauptschleife der Regula-Falsi-Methode, die so lange läuft, bis der Funktionswert an c kleiner als epsilon ist
    while abs(fc) >= epsilon:
        # Überprüfen, ob einer der Intervallgrenzen oder die Mitte die Nullstelle ist
        if fa == 0:
            return a, fa, accuracy_values, x_values
        elif fb == 0:
            return b, fb, accuracy_values, x_values
        elif fc == 0:
            return c, fc, accuracy_values, x_values
        
        # Bestimmen, in welchem Intervall die Nullstelle liegt und die Intervallgrenzen entsprechend anpassen
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        # Einziger Unterschied zur Bisektionsmethode: Berechnung der neuen Stelle c anhand der Regula-Falsi-Formel
        c = b - fb * ((b - a) / (fb - fa))
        fc = function(c, function_str)

        accuracy_values.append(abs(fc))
        x_values.append(c)
        
    return c, fc, accuracy_values, x_values


def test_solver2() -> None:
    """
    Testfunktion, die die Regula-Falsi-Methode mit verschiedenen Funktionen testet.

    Rückgabewerte:
        - None
    """

    # Testfälle mit verschiedenen Funktionen und Intervallen
    for n in [16, 15, 25, 81, 144]:
        function_str = f"x**2-{n}"
        a = 0
        b = n
        epsilon = 10**-8

        c, fc, accuracy_values, x_values = regula_falsi(function_str, a, b, epsilon)

        # Ausgabe der Ergebnisse für jeden Testfall
        print(f"\nTest für n = {n}")
        print(f"Numerisch: {c}")
        print(f"Analytisch: {n**0.5}")
        print(f"Ungenauigkeit: {abs(c - n**0.5)}")



if __name__ == "__main__":
    
    solver2()