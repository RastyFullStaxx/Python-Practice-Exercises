# Implement a quadratic equation solver.
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

a = 1
b = -3
c = 2
roots = solve_quadratic(a, b, c)
print(roots)
