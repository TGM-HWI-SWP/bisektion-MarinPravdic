from Aufgabe5 import get_inputs, get_epsilon, bisection
from Aufgabe6 import regula_falsi
import matplotlib.pyplot as plt



def plotter() -> None:
    """
    Hauptfunktion, die die Benutzereingaben entgegennimmt, die Nullstelle anhand der gewählten Methode berechnet, das Ergebnis ausgibt und den Fehlerverlauf sowie die aktuelle Lösung visualisiert.

    Rückgabewerte:
        - None
    """

    # Benutzeranweisungen
    print("\n=== Aufgabe 7: Grafische Darstellung ===")
    print("Dieses Programm visualisiert die Nullstellenberechnung.")
    print("Sie können zwischen Bisektion und Regula Falsi wählen.")
    print("Es werden die Genauigkeit und die Annäherung der Lösung grafisch dargestellt.")

    # Benutzereingaben entgegennehmen
    function_str, a, b = get_inputs()
    epsilon = get_epsilon()
    procedure = get_procedure()

    # Berechnung der Nullstelle basierend auf der gewählten Methode
    if procedure == 'b':
        c, fc, accuracy_values, x_values, iterations = bisection(function_str, a, b, epsilon)
    else:
        c, fc, accuracy_values, x_values = regula_falsi(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")

    visualisation(accuracy_values, x_values)


def get_procedure() -> str:
    """
    Funktion, die den Benutzer fragt, ob er die Bisektion-Methode oder die Regula-Falsi-Methode verwenden möchte.

    Rückgabewerte:
        - procedure (string): 'b' für Bisektion oder 'r' für Regula-Falsi
    """

    # Benutzer nach der gewünschten Methode fragen und die Eingabe validieren
    while True:
        procedure = input("\nMöchten Sie die Bisektion-Methode oder die Regula-Falsi-Methode verwenden? (b/r): ").lower()
        if procedure not in ['b', 'r']:
            print("\nUngültige Eingabe. Bitte geben Sie 'b' für Bisektion oder 'r' für Regula-Falsi ein.")
            continue
    
        return procedure


def visualisation(accuracy_values : list, x_values : list) -> None:
    """
    Funktion, die den Fehlerverlauf und die aktuelle Lösung während den Iterationen visualisiert.

    Parameter:
        - accuracy_values (list): Liste der Fehlerwerte (|f(c)|) für jede Iteration
        - x_values (list): Liste der aktuellen Lösungen c für jede Iteration

    Rückgabewerte:
        - None
    """

    fig, (graph1, graph2) = plt.subplots(2, 1, figsize=(16, 8))     # Erstellen von zwei Subplots: einer für den Fehlerverlauf und einer für die aktuelle Lösung
    fig.subplots_adjust(hspace=0.5)                                 # Abstand zwischen den Subplots anpassen

    # Animieren der Plots, indem in jeder Iteration die Fehlerwerte und aktuellen Lösungen bis zu diesem Punkt geplottet werden
    for i in range(len(accuracy_values)):
        # Plots löschen, um die neuen Werte zu aktualisieren
        graph1.clear()
        graph2.clear()

        # Fehlerverlauf und aktuelle Lösung bis zur aktuellen Iteration plotten
        graph1.plot(accuracy_values[:i+1])
        graph1.set_title("Genauigkeit")
        graph1.text(0.02, 0.9, f"Genauigkeit = {accuracy_values[i]:.6f}", transform=graph1.transAxes)   # Aktuellen Fehler als Text in der oberen linken Ecke des Plots anzeigen
        graph1.set_xlabel("Iteration")
        graph1.set_ylabel("|f(x)|")

        # Aktuelle Lösung x bis zur aktuellen Iteration plotten
        graph2.plot(x_values[:i+1])
        graph2.set_title("Aktuelle Lösung x")
        graph2.text(0.02, 0.9, f"x = {x_values[i]:.6f}", transform=graph2.transAxes)            # Aktuelle Lösung als Text in der oberen linken Ecke des Plots anzeigen
        graph2.set_xlabel("Iteration")
        graph2.set_ylabel("x")

        plt.pause(0.1)  # Kurze Pause, um die Animation sichtbar zu machen

    plt.show()



if __name__ == "__main__":
    
    plotter()