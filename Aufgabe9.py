from Aufgabe5 import bisection
from Aufgabe6 import regula_falsi
from Aufgabe7 import visualisation
import math


def electrical_line():
    curvature_str = "x * cosh(50/x) - x - 10"
    a = 100
    b = 200
    epsilon, procedure = get_inputs()

    if procedure == 'b':
        c, fc, error_values, x_values = bisection(curvature_str, a, b, epsilon)
    else:
        c, fc, error_values, x_values = regula_falsi(curvature_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")

    visualisation(error_values, x_values)

    length = 2 * c * math.sinh(50 / c)

    print(f"\nDer Krümmungsradius a beträgt: {c}m")
    print(f"Die Länge der elektrischen Leitung beträgt: {length}m")


def get_inputs():
    while True:
        try:
            epsilon_exp = int(input("Bitte geben Sie die gewünschte Genauigkeit ein (10^...): "))

            procedure = input("\nMöchten Sie die Bisection-Methode oder die Regula-Falsi-Methode verwenden? (b/r): ").lower()
            if procedure not in ['b', 'r']:
                print("\nUngültige Eingabe. Bitte geben Sie 'b' für Bisection oder 'r' für Regula-Falsi ein.")
                continue
            break
        
        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

    epsilon = 10**epsilon_exp

    return epsilon, procedure



if __name__ == "__main__":
    electrical_line()