#Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
#Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
#После чего опять просит угадать. И так пока пользователь не угадает выбранное число.

import random
programm_choice = random.randint(1, 10)

while True:
    user_choice = int(input("Введите число от 1 до 10:"))

    if user_choice == programm_choice:
        print("Вы угадали число")
        break

    valid_user_choice = 1 <= int(user_choice) <= 10

    if not valid_user_choice:
        print("Неверный ввод! Введите число от 1 до 10.")
        continue

    elif user_choice != programm_choice:
        print("Попробуйте еще раз")

