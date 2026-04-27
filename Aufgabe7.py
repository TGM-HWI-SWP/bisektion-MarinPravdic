import matplotlib.pyplot as plt
import numpy as np
from Aufgabe5 import bisection
from Aufgabe6 import regula_falsi


def plotter():
    function_str, a, b, epsilon, procedure = get_inputs()

    if procedure == 'b':
        c, fc, error_values, x_values = bisection(function_str, a, b, epsilon)
    else:
        c, fc, error_values, x_values = regula_falsi(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei x = {c} mit f(x) = {fc}")

    visualisation(error_values, x_values)


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


def function(x, function_str):
    return eval(function_str.replace('x', f'({x})'))


def bisection(function_str, a, b, epsilon):
    fa = function(a, function_str)
    fb = function(b, function_str)

    error_values = []
    x_values = []

    if fa * fb > 0:
        print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass die Nullstelle enthält.")
        exit()

    c = (a + b) / 2
    fc = function(c, function_str)

    while abs(fc) >= epsilon:
        error_values.append(c)
        x_values.append(abs(fc))

        if fa == 0:
            return a, fa
        elif fb == 0:
            return b, fb
        elif fc == 0:
            return c, fc

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = (a + b) / 2
        fc = function(c, function_str)

    return c, fc, error_values, x_values


def regula_falsi(function_str, a, b, epsilon):
    fa = function(a, function_str)
    fb = function(b, function_str)

    error_values = []
    x_values = []

    if fa * fb > 0:
        print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass eine Nullstelle enthält.")
        exit()

    c = b - fb * ((b - a) / (fb - fa))
    fc = function(c, function_str)

    while abs(fc) >= epsilon:
        error_values.append(c)
        x_values.append(abs(fc))

        if fa == 0:
            return a, fa
        elif fb == 0:
            return b, fb
        elif fc == 0:
            return c, fc
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = b - fb * ((b - a) / (fb - fa))
        fc = function(c, function_str)
        
    return c, fc, error_values, x_values


def visualisation(error_values, x_values):
    plt.figure(figsize=(10, 6))


if __name__ == "__main__":
    
    plotter()