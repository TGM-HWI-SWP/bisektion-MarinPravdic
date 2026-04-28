

def tester():
    function_str, a, b, epsilon = get_inputs()
    c, fc, iterations = bisection(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")
    print(f"Anzahl der Iterationen für Genauigkeit von {epsilon}: {iterations}")


def get_inputs():
    function_str = "2*x + x**2 + 3*x**3 - x**4"
    a = 2
    b = 5

    while True:
        try:
            epsilon_exp = int(input("Bitte geben Sie die gewünschte Genauigkeit ein (10^...): "))
            break
        
        except ValueError:
            print("\nUngültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

    epsilon = 10**epsilon_exp

    return function_str, a, b, epsilon


def function(x, function_str):
    return eval(function_str.replace('x', f'({x})'))


def bisection(function_str, a, b, epsilon):
    fa = function(a, function_str)
    fb = function(b, function_str)

    c = (a + b) / 2
    fc = function(c, function_str)

    iterations = 0

    while abs(fc) >= epsilon:
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = (a + b) / 2
        fc = function(c, function_str)

        iterations += 1

    return c, fc, iterations


if __name__ == "__main__":

    tester()