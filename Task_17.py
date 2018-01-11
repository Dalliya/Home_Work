#Написать функцию решения квадратного уравнения.
#def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
#pass

#a*(x**2) + b*x + c = 0

import math
a = int(input("Введите значение a = "))
b = int(input("Введите значение b = "))
c = int(input("Введите значение c = "))

def solve_quadratic_equation(a, b, c):
    if (b**2 - 4*a*c) > 0:
        result1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        result2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
        return result1, result2

result1, result2 = solve_quadratic_equation(a, b, c)
print(result1, result2)


