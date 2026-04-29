from Aufgabe5 import get_inputs, get_epsilon, bisection
from Aufgabe6 import regula_falsi
import matplotlib.pyplot as plt
import math



def plotter():
    function_str, a, b = get_inputs()
    epsilon = get_epsilon()
    procedure = get_procedure()

    if procedure == 'b':
        c, fc, error_values, x_values, iterations = bisection(function_str, a, b, epsilon)
    else:
        c, fc, error_values, x_values = regula_falsi(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei x = {c} mit f(x) = {fc}")

    visualisation(error_values, x_values)


def get_procedure():
    while True:
        procedure = input("\nMöchten Sie die Bisection-Methode oder die Regula-Falsi-Methode verwenden? (b/r): ").lower()
        if procedure not in ['b', 'r']:
            print("\nUngültige Eingabe. Bitte geben Sie 'b' für Bisection oder 'r' für Regula-Falsi ein.")
            continue
    
        return procedure


def visualisation(error_values, x_values):
    fig, (graph1, graph2) = plt.subplots(2, 1, figsize=(16, 8))
    fig.subplots_adjust(hspace=0.5)

    for i in range(len(error_values)):
        graph1.clear()
        graph2.clear()

        graph1.plot(error_values[:i+1])
        graph1.set_title("Fehlerverlauf")
        graph1.set_xlabel("Iteration")
        graph1.set_ylabel("|f(x)|")

        graph2.plot(x_values[:i+1])
        graph2.set_title("Aktuelle Lösung x")
        graph2.set_xlabel("Iteration")
        graph2.set_ylabel("x")

        plt.pause(0.1)

    plt.show()


if __name__ == "__main__":
    
    plotter()