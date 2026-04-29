import math


def solver():
    test_solver()

    function_str, a, b = get_inputs()
    epsilon = get_epsilon()
    c, fc, error_values, x_values, iterations = bisection(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")


def get_inputs():
    function_str = input("\nBitte geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

    while True:
        try:
            a = float(input("\nBitte geben Sie die erste Intervallsgrenze ein: "))
            b = float(input("Bitte geben Sie die zweite Intervallsgrenze ein: "))
            break
        
        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

    if a >= b:
        print("\nDie erste Intervallsgrenze muss kleiner als die zweite sein.")
        exit()

    return function_str, a, b


def get_epsilon():
    while True:
        try:
            epsilon_exp = int(input("\nBitte geben Sie die gewünschte Genauigkeit ein (10^...): "))
            break
        
        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
    
    epsilon = 10**epsilon_exp

    return epsilon


def function(x, function_str):
    return eval(function_str, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sinh": math.sinh,
        "cosh": math.cosh,
        "exp": math.exp,
        "sqrt": math.sqrt,
        "log": math.log,
        "pi": math.pi,
        "e": math.e
    })


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

    error_values.append(abs(fc))
    x_values.append(c)
    
    iterations = 0

    while abs(fc) >= epsilon:
        if fa == 0:
            return a, fa, error_values, x_values, iterations
        elif fb == 0:
            return b, fb, error_values, x_values, iterations
        elif fc == 0:
            return c, fc, error_values, x_values, iterations

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = (a + b) / 2
        fc = function(c, function_str)

        error_values.append(abs(fc))
        x_values.append(c)

        iterations += 1

    return c, fc, error_values, x_values, iterations


def test_solver():
    for n in [25, 81, 144]:
        function_str = f"x**2-{n}"
        a = 0
        b = n
        epsilon = 10**-8

        c, fc, error_values, x_values, iterations = bisection(function_str, a, b, epsilon)

        print(f"\nTest für n = {n}")
        print(f"Numerisch: {c}")
        print(f"Analytisch: {n**0.5}")
        print(f"Ungenauigkeit: {abs(c - n**0.5)}")


if __name__ == "__main__":

    solver()