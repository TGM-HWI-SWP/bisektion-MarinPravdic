from Aufgabe5 import bisection, get_epsilon
from Aufgabe6 import regula_falsi
from Aufgabe7 import get_procedure, visualisation
import math


def electrical_line():
    curvature_str = "x * cosh(50/x) - x - 10"
    a = 100
    b = 200
    epsilon = get_epsilon()
    procedure = get_procedure()

    if procedure == 'b':
        c, fc, error_values, x_values, iterations = bisection(curvature_str, a, b, epsilon)
    else:
        c, fc, error_values, x_values = regula_falsi(curvature_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")

    visualisation(error_values, x_values)

    length = 2 * c * math.sinh(50 / c)

    print(f"\nDer Krümmungsradius a beträgt: {c}m")
    print(f"Die Länge der elektrischen Leitung beträgt: {length}m")


if __name__ == "__main__":
    electrical_line()