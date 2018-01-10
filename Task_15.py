import math

x1 = int(input("Введите координаты центра первой окружности:"))
y1 = int(input("Введите координаты центра первой окружности:"))
x2 = int(input("Введите координаты центра второй окружности:"))
y2 = int(input("Введите координаты центра второй окружности:"))
r1 = int(input("Введите радиус первой окружности:"))
r2 = int(input("Введите радиус второй окружности:"))

def circles_intersects(x1, y1, r1, x2, y2, r2):
    return (r1 + r2) > math.fabs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print(circles_intersects(x1, y1, r1, x2, y2, r2))
