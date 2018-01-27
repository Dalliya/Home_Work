#Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры
from functools import reduce
number = input("Введите пятизначное целое число: ")


def product_of_numbers(number):
    digit_list = []
    for i in str(number):
        if int(i) % 2 != 0:
            digit_list.append(int(i))
    print(digit_list)
    result = reduce(lambda x, y: x*y, digit_list)
    return result

print(product_of_numbers(number))











