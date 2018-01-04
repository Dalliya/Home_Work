import math

catheter1 = a = int(input("Введите катет 1 прямоугольного треугольника:"))
catheter2 = b = int(input("Введите катет 2 прямоугольного треугольника:"))

def triangle_square_and_perimeter(a, b):
    result = (a * b / 2), (a + b + math.sqrt(a**2 + b**2))
    return result

result = triangle_square_and_perimeter(a, b)
print(result)



