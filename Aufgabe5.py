

def solver():
    function_str, a, b, epsilon = get_inputs()
    c, fc = bisection(function_str, a, b, epsilon)

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}, Funktionswert: {fc}")
    print(f"Restintervall: [{a}, {b}]")


def get_inputs():
    function_str = input("Bitte geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

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
    c = (a + b) / 2
    fc = function(c, function_str)

    while abs(fc) >= epsilon:
        fa = function(a, function_str)
        fb = function(b, function_str)

        if fa * fb > 0:
            print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass die Nullstelle enthält.")
            exit()

        if fa == 0:
            print(f"Exakte Nullstelle bei a: {a}")
            return
        elif fb == 0:
            print(f"Exakte Nullstelle bei b: {b}")
            return
        elif fc == 0:
            print(f"Exakte Nullstelle bei c: {c}")
            return

        if fa * fc < 0:
            b = c
        else:
            a = c

        c = (a + b) / 2
        fc = function(c, function_str)

    return c, fc



if __name__ == "__main__":
    
    solver()