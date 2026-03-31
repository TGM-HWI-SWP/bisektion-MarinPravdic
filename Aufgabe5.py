

def solver():
    function = input("Bitte geben Sie die Funktion f(x) ein (z.B. 'x**2 - 4'): ")

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
        return

    while True:
        fa = eval(function.replace('x', f'({a})'))
        fb = eval(function.replace('x', f'({b})'))

        if fa * fb > 0:
            print("\nUngültiges Intervall. Bitte wählen Sie ein Intervall, dass die Nullstelle enthält.")
            return

        c = (a + b) / 2
        fc = eval(function.replace('x', f'({c})'))

        if abs(b - a) < epsilon:
            break
        
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

    print(f"\nDie Nullstelle liegt näherungsweise bei: {c}")
    print(f"Restintervall: [{a}, {b}]")



if __name__ == "__main__":
    
    solver()