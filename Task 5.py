import math

a = 19
b = 156
c = 1

result = math.fabs(a - b) / (a + b)**3 - math.cos(c)

print("Результат выражения |a - b| / ( a + b)**3 - cos(c) при a = %d , b = %d и c = %d равен: %.5f" % (a, b, c, result))







