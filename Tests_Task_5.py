#Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
#Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.


import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))

if abs(10 - x) > abs(10 - y):
        print(y)
elif abs(10 - y) > abs(10 - x):
        print(x)




