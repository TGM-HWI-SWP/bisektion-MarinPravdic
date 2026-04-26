import matplotlib.pyplot as plt
import numpy as np
from Aufgabe5 import bisection
from Aufgabe6 import regula_falsi


def plotter():
    function_str, a, b, epsilon, procedure = get_inputs()

    if procedure == 'b':
        c, fc = bisection(function_str, a, b, epsilon)
    else:
        c, fc = regula_falsi(function_str, a, b, epsilon)


def get_inputs():
    function_str = input("\nBitte geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

    while True:
        try:
            a = float(input("\nBitte geben Sie die erste Intervallsgrenze ein: "))
            b = float(input("Bitte geben Sie die zweite Intervallsgrenze ein: "))
            epsilon_exp = int(input("Bitte geben Sie die gewünschte Genauigkeit ein (10^...): "))

            procedure = input("\nMöchten Sie die Bisection-Methode oder die Regula-Falsi-Methode verwenden? (b/r): ").lower()
            if procedure not in ['b', 'r']:
                print("\nUngültige Eingabe. Bitte geben Sie 'b' für Bisection oder 'r' für Regula-Falsi ein.")
                continue
            break

        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

    epsilon = 10**epsilon_exp

    if a >= b:
        print("\nDie erste Intervallsgrenze muss kleiner als die zweite sein.")
        exit()

    return function_str, a, b, epsilon, procedure


if __name__ == "__main__":
    
    plotter()