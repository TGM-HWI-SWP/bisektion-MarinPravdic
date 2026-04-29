from Aufgabe5 import bisection, get_epsilon
from Aufgabe6 import regula_falsi
from Aufgabe7 import get_procedure, visualisation
import math



def electrical_line() -> None:
    """
    Hauptfunktion, die die Kettenlinie für eine elektrische Leitung berechnet. Es wird die Nullstelle der Funktion "x * cosh(50/x) - x - 10" bestimmt, um den Krümmungsradius a zu finden, und anschließend die Länge der Leitung berechnet.

    Rückgabewerte:
        - None
    """

    # Funktion für die Kettenlinie (Nullstelle für a/x) und Intervalle für die Berechnung
    curvature_str = "x * cosh(50/x) - x - 10"
    a = 100
    b = 200

    # Benutzereingaben entgegennehmen
    epsilon = get_epsilon()
    procedure = get_procedure()

    # Berechnung der Nullstelle basierend auf der gewählten Methode
    if procedure == 'b':
        c, fc, error_values, x_values, iterations = bisection(curvature_str, a, b, epsilon)
    else:
        c, fc, error_values, x_values = regula_falsi(curvature_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")

    visualisation(error_values, x_values)     # Visualisierung des Fehlerverlaufs und der aktuellen Lösung während der Iterationen für den Krümmungsradius a

    length = 2 * c * math.sinh(50 / c)       # Berechnung der Länge der elektrischen Leitung basierend auf dem gefundenen Krümmungsradius a (c) und der Formel für die Kettenlinie

    print(f"\nDer Krümmungsradius a beträgt: {c}m")
    print(f"Die Länge der elektrischen Leitung beträgt: {length}m")



if __name__ == "__main__":

    electrical_line()