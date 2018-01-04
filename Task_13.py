import math

a = int(input())
b = int(input())

def triangle_square_and_perimeter(a, b):
    result = float(a * b / 2), float(a + b + math.sqrt(a**2 + b**2))
    return result

result = triangle_square_and_perimeter(a, b)
print(result)



