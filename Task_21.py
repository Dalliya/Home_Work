#Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
#def get_max_digit(number): # returns int
#		     pass


import random

number = random.randint(1e11, 1e12-1)
print(number)

def get_max_digit(number):
    digit_list = []
    for i in str(number):
        digit_list.append(i)
    max_digit = max(digit_list)
    return max_digit

print(get_max_digit(number))








