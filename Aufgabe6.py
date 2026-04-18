

def solver2():
    function_str, a, b, epsilon = get_inputs()
    c, fc = regula_falsi(function_str, a, b, epsilon)


def get_inputs():
    function_str = input("\nBitte geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

    while True:
        try:
            a = float(input("\nBitte geben Sie die erste Intervallsgrenze ein: "))
            b = float(input("Bitte geben Sie die zweite Intervallsgrenze ein: "))
            epsilon_exp = int(input("Bitte geben Sie die gewünschte Genauigkeit ein (10^...): "))
            break

        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

    epsilon = 10**epsilon_exp

    if a >= b:
        print("\nDie erste Intervallsgrenze muss kleiner als die zweite sein.")
        exit()

    return function_str, a, b, epsilon


def function(x, function_str):
    return eval(function_str.replace('x', f'({x})'))


def regula_falsi(function_str, a, b, epsilon):
    fa = function(a, function_str)
    fb = function(b, function_str)

    if fa * fb > 0:
        print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass eine Nullstelle enthält.")
        exit()


if __name__ == "__main__":
    
    solver2()