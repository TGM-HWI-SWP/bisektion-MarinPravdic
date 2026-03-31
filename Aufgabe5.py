

def solver():
    function = input("Geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

    a = float(input("\nGeben Sie die erste Intervallsgrenze ein: "))
    b = float(input("Geben Sie die zweite Intervallsgrenze ein: "))
    epsilon_exp = int(input("Bitte geben Sie die gewünschte Genauigkeit ein (10^...): "))

    epsilon = 10**epsilon_exp

    while True:
        fa = eval(function.replace('x', str(a)))
        fb = eval(function.replace('x', str(b)))

        if fa * fb > 0:
            print("Ungültiges Intervall. Bitte wählen Sie ein Intervall, dass die Nullstelle enthält.")
            break

        c = (a + b) / 2
        fc = eval(function.replace('x', str(c)))

        if abs(b - a) < epsilon:
            break

        if fc == 0:
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}")
    print(f"Restintervall: [{a}, {b}]")



if __name__ == "__main__":
    
    solver()