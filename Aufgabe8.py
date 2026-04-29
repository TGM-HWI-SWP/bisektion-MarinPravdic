

def tester():
    function_str = "2*x + x**2 + 3*x**3 - x**4"
    a = 2
    b = 5

    for epsilon in [10**-2, 10**-8]:
        c, fc, iterations = bisection(function_str, a, b, epsilon)

        print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")
        print(f"Anzahl der Iterationen für Genauigkeit von {epsilon}: {iterations}")
        print(f"Abweichung von der tatsächlichen Nullstelle: {abs(c - 3.4567)}")


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