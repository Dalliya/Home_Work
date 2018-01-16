#Написать функцию решения квадратного уравнения.
#def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
#pass

#a*(x**2) + b*x + c = 0

import math

a = float(input("Введите значение a = "))
b = float(input("Введите значение b = "))
c = float(input("Введите значение c = "))

def solve_quadratic_equation(a, b, c):
    D = b**2 - 4*a*c
    if D > 0 and a != 0:
        result_1 = (-b + math.sqrt(D)) / (2 * a)
        result_2 = (-b - math.sqrt(D)) / (2 * a)
        return result_1, result_2

    if D == 0:
        result = -b / (2 * a)
        return result, None

    else:
        return None, None

print(solve_quadratic_equation(a, b, c))



