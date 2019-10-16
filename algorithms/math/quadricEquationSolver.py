import math as m

def quadricEquationSolver(a, b, c):
    # If a is 0, then equation is
    # not quadratic, but linear
    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = m.sqrt(abs(d))
    if d > 0:
        print("Roots are real and different ")
        x1 = ((- b + sqrt_val) / (2 * a))
        x2 = ((- b - sqrt_val) / (2 * a))
    elif d == 0:
        print("Roots are real and same")
        x1 = x2 = (- b / (2 * a))
    else:
        print("Roots are complex")
        x1 = (- b / (2 * a), " + i", sqrt_val)
        x2 = (- b / (2 * a), " - i", sqrt_val)
    return x1,x2

roots = quadricEquationSolver(1, -7, 12)
print(roots)
