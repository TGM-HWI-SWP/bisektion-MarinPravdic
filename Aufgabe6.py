from Aufgabe5 import get_inputs, get_epsilon, function


def solver2():
    test_solver2()

    function_str, a, b = get_inputs()
    epsilon = get_epsilon()
    c, fc, error_values, x_values = regula_falsi(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")


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

    error_values.append(abs(fc))
    x_values.append(c)

    while abs(fc) >= epsilon:
        if fa == 0:
            return a, fa, error_values, x_values
        elif fb == 0:
            return b, fb, error_values, x_values
        elif fc == 0:
            return c, fc, error_values, x_values
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = b - fb * ((b - a) / (fb - fa))
        fc = function(c, function_str)

        error_values.append(abs(fc))
        x_values.append(c)
        
    return c, fc, error_values, x_values


def test_solver2():
    for n in [16, 15, 25, 81, 144]:
        function_str = f"x**2-{n}"
        a = 0
        b = n
        epsilon = 10**-8

        c, fc, error_values, x_values = regula_falsi(function_str, a, b, epsilon)

        print(f"\nTest für n = {n}")
        print(f"Numerisch: {c}")
        print(f"Analytisch: {n**0.5}")
        print(f"Ungenauigkeit: {abs(c - n**0.5)}")



if __name__ == "__main__":
    
    solver2()