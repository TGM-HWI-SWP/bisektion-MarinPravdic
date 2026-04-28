

def tester():
    function_str, a, b, epsilon = get_inputs()
    c, fc = bisection(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")


def get_inputs():
    function_str = "2*x + x**2 + 3*x**3 - x**4"

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


def bisection(function_str, a, b, epsilon):
    fa = function(a, function_str)
    fb = function(b, function_str)

    if fa * fb > 0:
        print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass die Nullstelle enthält.")
        exit()

    c = (a + b) / 2
    fc = function(c, function_str)

    while abs(fc) >= epsilon:
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

    return c, fc


if __name__ == "__main__":

    tester()